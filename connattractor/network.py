# https://github.com/takyamamoto/Hopfield-Network

from dataclasses import dataclass
import numpy as np
import warnings
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import random
from tqdm import tqdm
from nilearn import image, plotting
from nibabel.processing import resample_from_to
import nibabel as nib
from itertools import combinations, permutations

from . import config



class State(np.ndarray):

    def __new__(cls, input, labelmap=None):
        if isinstance(input, nib.nifti2.Nifti2Image) or isinstance(input, nib.nifti1.Nifti1Image) or isinstance(input,
                                                                                                                str):
            # it's a nifti
            if not labelmap:
                labelmap = config.DEFAULT_ATLAS_NII
            obj = np.asarray(State._from_Nifti1Image(input, labelmap)).view(cls)
        else:
            obj = np.asarray(input).view(cls)
        obj.labelmap = labelmap
        return obj  # .astype(np.float128)

    def __array_finalize__(self, obj):
        if obj is None: return
        self.labelmap = getattr(obj, 'info', None)

    def __array_wrap__(self, out_arr, context=None):
        # just call the parent
        return super(State, self).__array_wrap__(self, out_arr, context)

    def _from_Nifti1Image(nii,
                          labelmap=config.DEFAULT_ATLAS_NII,
                          ):

        if isinstance(labelmap, str):
            # it's a file name
            atlas_data = nib.load(labelmap)
        else:
            atlas_data = labelmap

        if isinstance(nii, str):
            # it's a file name
            map_data = nib.load(nii)
        else:
            map_data = nii

        map_data = resample_from_to(map_data, atlas_data, order=2)
        map_data = map_data.get_fdata()
        atlas_data = atlas_data.get_fdata()

        M = int(np.max(atlas_data))

        ret = np.zeros(M)
        for l in range(1, M + 1):
            indices = np.argwhere(atlas_data == l)
            X = []
            for i in indices:
                x = map_data[i[0], i[1], i[2]]
                X.append(x.tolist())
            X = np.array(X)
            if X.shape[0] == 0:
                x = 0
            elif X.shape[0] == 1:
                x = X.flatten()
            x = np.mean(X, axis=0)
            ret[l - 1] = x

        ret = np.transpose(np.array(ret))
        return (ret)

    def to_Nifti1Image(self,
                       labelmap=config.DEFAULT_ATLAS_NII,
                       outfile=""):
        # todo: fix this
        # if self.shape[0] != config.DEAFULT_ATLAS_M:
        #    print(str(self.shape[0]) + " " + str(config.DEAFULT_ATLAS_M))
        #    raise ValueError('Please adjust the labelmap for image conversion!')
        img = image.load_img(labelmap)

        lut = self
        lut = np.array([0] + lut.tolist())  # for background

        data = img.get_fdata()
        newdata = lut[np.array(data, dtype=np.int32)]  # apply lookup table to swap labels
        volume = nib.Nifti1Image(newdata.astype(np.float64), img.affine)

        if outfile:
            # save
            nib.save(volume, outfile)
        return volume

    def plot(self, smooth=6, labelmap=config.MIST122_NII, **kwargs):
        img = self.to_Nifti1Image(labelmap)

        if smooth > 0:
            smooth_img = image.smooth_img(img, fwhm=smooth)
        else:
            smooth_img = img

        default_plot_kwargs = {
            'display_mode': 'lyrz',
            'colorbar': True,
            'plot_abs': False,
            'cmap': cm.coolwarm
        }
        default_plot_kwargs.update(kwargs)

        return plotting.plot_glass_brain(smooth_img, **default_plot_kwargs)


class Hopfield(object):
    def __init__(self, input, threshold=0, beta=0.1, scale=False):
        if isinstance(input, int):
            # number of neurons
            self.num_neuron = input
            self.W = np.zeros(input, input)
        elif input.shape[0] == input.shape[1]:
            self.W = input
            self.num_neuron = input.shape[0]
            # Make diagonal element of W into 0
            diagW = np.diag(np.diag(self.W))
            self.W = self.W - diagW
            if scale:
                self.W = (self.W - np.mean(self.W)) / np.std(self.W)
        self.threshold = threshold
        self.beta = beta

        # initilaize with empty state
        self._state = State(np.zeros(self.num_neuron))

    def train_weights(self, train_data):  # tarin_data is a list of States
        num_data = len(train_data)
        self.num_neuron = train_data[0].shape[0]

        # initialize weights
        W = np.zeros((self.num_neuron, self.num_neuron))
        rho = np.sum([np.sum(t) for t in train_data]) / (num_data * self.num_neuron)

        # Hebb rule
        for i in tqdm(range(num_data)):
            t = train_data[i] - rho
            W += np.outer(t, t)

        # Make diagonal element of W into 0
        diagW = np.diag(np.diag(W))
        W = W - diagW
        W /= num_data

        self.W = W

    def set_weights(self, W,
                    scale=False):  # set weight manually, e.g. ti initilaize it with an empirical functional connectome
        # Make diagonal element of W into 0
        diagW = np.diag(np.diag(W))
        W = W - diagW
        if scale:
            W = (W - np.mean(W)) / np.std(W)
        self.W = W
        self.num_neuron = W.shape[0]

    def get_state(self):
        return np.arctanh(self._state)

    def update(self, state, threshold=None, beta=None, num_iter=10000, asyn=False, seed=None, verbose=False, plot=0,
               plot_tolerance=.9999):
        if threshold:
            self.threshold = threshold  # override threshold
        if beta:
            self.beta = beta  # override beta

        self.num_iter = num_iter
        self.asyn = asyn

        # if verbose:
        #    print("Running Hopfield Network until convergence to attractor state...")

        # Copy to avoid call by reference
        # todo: make the sigmoid optional?
        # sigmoid transformation to initialize the state
        state = np.tanh(state)

        self._state = State(np.copy(state))  # copy?

        energy_conv = []

        if self.asyn == False:
            """
            Synchronous update
            """

            # Compute initial state energy
            # e = self.energy_cont(self.state)
            e = self.energy(self._state)

            energy_conv.append(e)

            # Iteration
            pbar = tqdm(range(self.num_iter), disable=not verbose)
            for i in pbar:
                if plot > 0 and not i % plot:
                    print("Iter: " + str(i) + " Energy: " + str(e))
                    self.plot_activation()
                # Update s
                # act. flow a_i=sum(w_ij*a_j) j!=i
                # s = np.sign(self.W @ s - self.threshold)
                # print(self.W)
                # print(self.state)
                # print(self.W @ np.array(self.state))
                # self.state = State(np.tanh(self.beta * (self.W @ np.array(self.state) - self.threshold)))  # continous
                self._state = State(np.tanh(self.beta * (self.W @ np.array(self._state) - self.threshold)))  # continous

                # Compute new state energy
                # e_new = self.energy_cont(self.state)
                e_new = self.energy(self._state)

                energy_conv.append(e_new)
                # unique_states = count_unique_states(np.asarray(q_states), atol=0, rtol=1e-10)[0]

                # if plot and plot_tolerance <= e / e_new:
                #    plot = -1  # The end is boring, don't plot it!

                pbar.set_description("Energy: %f" % e_new)

                if e == e_new:  # ToDo: introduce a tolerance?
                    if verbose:
                        print("Converged. Energy: " + str(e) + " Iteration: " + str(i))
                    if plot != 0:
                        print("Converged. Energy: " + str(e) + " Iteration: " + str(i))
                        self.plot_activation()
                    return np.arctanh(self._state), i + 1, energy_conv  # converged
                # Update energy
                e = e_new
            # return NaN if energy does not converge
            # warnings.warn("Warning: Hopfield Network did not converge! Consider increasing num_iter.")
            # empty_state = np.empty(np.shape(self.state))
            # empty_state[:] = np.nan
            # return empty_state, i + 1  # No convergence, still you can get the state with get_sate()
            return np.arctanh(
                self._state), i + 1, energy_conv  # No convergence, still you can get the state with get_sate()
        else:
            """
            Asynchronous update
            """
            raise Warning("Asynchronous update is not tested yet!")
            # Compute initial state energy
            e = self.energy_cont(self._state)

            # Iteration
            pbar = tqdm(range(self.num_iter), disable=not verbose)
            for i in pbar:
                if plot > 0 and not i % plot:
                    print("Iter: " + str(i) + " Energy: " + str(e))
                    self.plot_activation()
                region_idx = list(range(len(self._state)))
                if seed is not None:
                    random.seed(seed)
                    random.shuffle(region_idx)
                for idx in region_idx:
                    # Update s
                    self._state[idx] = np.tanh(self.beta * (np.sum(
                        [self.W[i, idx] * self._state[i] for i in range(len(self._state))]) - self.threshold))

                # Compute new state energy
                # todo: change me back
                e_new = self.energy_cont(self._state)
                pbar.set_description("Energy: %f" % e_new)

                if plot > 0 and plot_tolerance <= e / e_new:
                    plot = -1

                # state has converged
                if e == e_new:  # ToDo: introduce a tolerance?
                    if verbose:
                        print("Converged. Energy: " + str(e) + " Iteration: " + str(i))
                    if plot != 0:
                        print("Converged. Energy: " + str(e) + " Iteration: " + str(i))
                        self.plot_activation()
                    return np.arctanh(self._state), i + 1  # converged
                # Update energy
                e = e_new
            warnings.warn("Warning: Hopfield Network did not converge! Consider increasing num_iter.")
            # todo: not a very elegant return value. Could number of iterations be a filed of the state?
            # can be None for states not being a result of relaxation
            return np.arctanh(self._state), i + 1  # No convergence, still you can get the state with get_sate()

    def energy(self, s):
        s = np.array(s)
        return -0.5 * s @ self.W @ s + np.sum(s * self.threshold)

    def plot_activation(self, smooth=6, arctanh=True, **kwargs):
        if arctanh:
            s = State(np.arctanh(np.array(self._state)))
        else:
            s = self._state
        s.plot(smooth=smooth, **kwargs)

    def plot_weights(self, **kwargs):
        # todo: return the plot isntead of showing it
        plt.figure(figsize=(6, 5))
        w_mat = plt.imshow(self.W, cmap=cm.coolwarm, **kwargs)
        plt.colorbar(w_mat)
        plt.title("Network Weights")
        plt.tight_layout()
        # plt.savefig("weights.png")
        #plt.show()


def fun_random_shuffle(prev_state):  # changes prev_state!
    np.random.shuffle(prev_state)
    return prev_state


def count_unique_states(att_states, rtol=1e-05, atol=1e-08):
    # count attractor states
    unique = []
    counts = []
    for i in range(att_states.shape[0]):
        found = False
        for j in range(len(unique)):
            if all(np.isclose(unique[j], att_states[i, :], rtol=rtol, atol=atol, equal_nan=False)):
                found = True
                counts[j] = counts[j] + 1
                break
        if not found:
            unique.append(att_states[i, :])
            counts.append(1)
    return unique, counts


def min_energy(hopfiled_network, state):
    # get the minumum energy with scaling the state
    raise Warning("Not implemented yet!")


def map_out_attractors(hopfiled_net,
                       base_state=None,
                       shuffle_iter=100,
                       hopfiled_num_iter=100000,
                       fun_state_gen=fun_random_shuffle,
                       sparsity=10,  # only if base_state=None
                       verbose=False
                       ):
    if not isinstance(base_state, np.ndarray):
        # init a simple sparse base state to be shuffled
        base_state = np.concatenate((np.repeat(0.1, sparsity), np.repeat(0, hopfiled_net.num_neuron - sparsity)),
                                    axis=0)

    iters = np.zeros(shuffle_iter)
    stim = np.zeros(shape=(shuffle_iter, hopfiled_net.num_neuron))
    act = np.zeros(shape=(shuffle_iter, hopfiled_net.num_neuron))

    if shuffle_iter == 1:
        act[0, :], iters[0] = hopfiled_net.update(base_state, num_iter=hopfiled_num_iter)[:2]
    else:
        for rand_stim_i in tqdm(range(shuffle_iter), disable=not verbose):
            stim[rand_stim_i, :] = fun_state_gen(base_state)
            act[rand_stim_i, :], iters[rand_stim_i] = hopfiled_net.update(stim[rand_stim_i, :],
                                                                          num_iter=hopfiled_num_iter)[:2]

    unique, counts = count_unique_states(act)

    if verbose:
        print("Number of attractor states:" + str(len(unique)))

    return len(unique), unique, counts, iters


def delete_inverse_states(attractors):
    # todo: compare number of input and output states, if comparison is too strict
    if len(attractors) % 2 != 0:
        warnings.warn('Uneven number of states. Check convergence!')
        # todo: link to convergence failure
        return

    state_perms = list(permutations(attractors, 2))
    states = []
    for state_pair in state_perms:

        if np.isclose(np.corrcoef(state_pair[0], state_pair[1])[0, 1], -1, atol=1e-09):
            if sum(state_pair[0]) >= 0 and sum(state_pair[1]) < 0:
                states.append(state_pair[0])
            elif sum(state_pair[0]) < 0 and sum(state_pair[1]) >= 0:
                states.append(state_pair[1])
            else:
                warnings.warn('no clear distinction to inverse state')
                states.append(state_pair[0])

    # todo: floor sum values to make it more robust
    _, idx = np.unique(np.sum(states, 1), return_index=True)
    unique_states = [states[i] for i in idx]

    return unique_states


def get_n_attractor_states(hopfield_net,
                           state_iter_max=50,
                           n_target_states=2,
                           beta_upper=0.1,
                           beta_lower=0,
                           verbose=True):
    # todo: fix the double calculating of the hopfield states
    hopfield_net.beta = beta_lower
    n_states_lower = map_out_attractors(hopfield_net)[0]

    hopfield_net.beta = beta_upper
    n_states_upper = map_out_attractors(hopfield_net)[0]

    while n_target_states > n_states_upper or n_target_states < n_states_lower:
        # print('warning, beta bounds changed')
        if n_target_states > n_states_upper:
            beta_upper *= 2
            hopfield_net.beta = beta_upper
            n_states_upper = map_out_attractors(hopfield_net)[0]
            print('beta upper', beta_upper)
            print('n states upper', n_states_upper)


        elif n_target_states < n_states_lower:
            beta_lower *= 0.5
            hopfield_net.beta = beta_lower
            n_states_lower = map_out_attractors(hopfield_net)[0]
            print('beta lower', beta_lower)
            print('n states lower', n_states_lower)

    beta = 0.5 * (beta_lower + beta_upper)
    hopfield_net.beta = beta
    n_states, attractors, counts, iters = map_out_attractors(hopfield_net)

    iter = 0

    while n_target_states is not n_states and iter < state_iter_max:
        if n_states > n_target_states:
            beta_upper = beta
        elif n_states < n_target_states:
            beta_lower = beta

        beta = 0.5 * (beta_lower + beta_upper)
        hopfield_net.beta = beta

        n_states, attractors, counts, iters = map_out_attractors(hopfield_net)
        iter += 1

    if verbose:
        print('beta iterations: ', iter)
        print('target beta: ', beta)

    return attractors, beta, iter
