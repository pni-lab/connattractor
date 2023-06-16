import numpy as np
from . import network
from tqdm import tqdm
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


def simulate_activations(connectome, noise_coef=1, num_iter=1000, calculate_attractors=True, init_state=None,
                         random_state=None, **kwargs):
    """
    Simulate activations of a Hopfield network  with a given connectome.
    :param connectome: a 2D numpy array
    :param noise_coef:  noise coefficient
    :param num_iter: number of iterations
    :param calculate_attractors: whether to calculate attractors
    :param init_state: initial state
    :param random_state: random state
    :param kwargs: additional arguments to network.Hopfield
    :return: states, attractors, energies, statedict
    """

    random = np.random.default_rng(random_state)

    default_kwargs = {
        "scale": True,
        "threshold": 0,
        "beta": 0.05
    }
    default_kwargs.update(kwargs)
    hopnet = network.Hopfield(connectome, **default_kwargs)

    states = np.zeros((num_iter + 1, hopnet.num_neuron))
    attractors = np.zeros(num_iter + 1)
    energies = np.zeros(num_iter + 1)

    statedict = dict()

    if init_state is None:
        states[0] = network.State(random.normal(0, 1, hopnet.num_neuron))
    else:
        states[0] = network.State(init_state)
    energies[0] = hopnet.energy(np.tanh(states[0]))

    for i in tqdm(range(num_iter)):
        new_state, n_iter, energy = hopnet.update(states[i], num_iter=1)
        energies[i] = energy[-1]

        if calculate_attractors:
            att, n_iter, energy = hopnet.update(states[i], num_iter=100000)
            if n_iter == 100000:
                print(n_iter, '!!')
                raise RuntimeWarning("Convergence error")
        else:
            att = None

        if tuple(np.round(att, 6)) not in statedict.keys():
            statedict[tuple(np.round(att, 4))] = len(statedict)
            attractors[i] = len(statedict) - 1
        else:
            attractors[i] = statedict[tuple(np.round(att, 4))]

        # add noise
        states[i + 1] = np.array(new_state) + np.random.normal(0, noise_coef, hopnet.num_neuron)

    return states, attractors, energies, statedict


def create_embeddings(states, **kwargs):
    """
    Create embeddings of a connectome.
    :param kwargs:
    :return:
    """

    pca = PCA(**kwargs)
    pca.fit_transform(states)
    return pca


def plot_embeddings(embedding, states, **kwargs):
    """
    Plot embeddings of a connectome.
    :param embedding: fitted sklearn estimator, e.g. PCA
    :param states: brain states
    :param kwargs: additional arguments to matplotlib.pyplot.scatter, e.g. c=attractors
    :return: matplotlib axes
    """

    emb = embedding.transform(states)
    ax = sns.scatterplot(x=emb[:, 0], y=emb[:, 1], **kwargs)
    return ax
