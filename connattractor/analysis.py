import pickle
import numpy as np
import sklearn.base
from matplotlib.figure import figaspect
from sklearn.linear_model import LogisticRegression
from dataclasses import dataclass
from collections import namedtuple

from sklearn.preprocessing import StandardScaler

from . import network
from tqdm import tqdm
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.ndimage import gaussian_filter


def _cart2pol(x, y):
    rho = np.sqrt(x ** 2 + y ** 2)
    phi = np.arctan2(y, x)  # * 180 / np.pi
    return rho, phi


def _pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


@dataclass
class HopfieldSimulation:
    hopnet: network.Hopfield
    states: np.ndarray
    energies: np.ndarray

    def save(self, filename):
        """
        Save HopfieldSimulation object with pickle.
        :param filename:
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)


@dataclass
class HopfiledEmbedding:
    hopnet: network.Hopfield
    embedding_model: sklearn.base.BaseEstimator
    attractors: dict
    attractor_model: sklearn.base.BaseEstimator
    attractor_model_dim: int
    state_sample: np.ndarray
    attractor_sample: np.ndarray

    def save(self, filename):
        """
        Save HopfieldEmbedding with pickle.
        :param filename:
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def plot(self,
             activations=None,
             plot_type='scatter',
             legend=True,
             density_bins=1000,
             density_sigma=20,
             ax=None,
             regimes_fill_kwargs=dict(),
             regimes_contour_kwargs=dict(),
             attractor_plot_type='scatter',
             attractor_kwargs=dict(),
             legend_kwargs=None,
             **kwargs):
        """
        Plot the attractor regimes and the data in the embedding space.
        :param activations: activations to plot
        :param regimes_fill_kwargs: kwargs for attractor regimes fill
        :param regimes_line_kwargs: kwargs for attractor regimes line
        :param ax: matplotlib axis (with polar projection)
        :param kwargs: kwargs for embedding model plot
        """

        default_regimes_fill_kwargs = dict(alpha=.2, cmap='tab10')
        default_regimes_fill_kwargs.update(regimes_fill_kwargs)

        default_regimes_contour_kwargs = dict(colors="gray", linewidths=0.5)
        default_regimes_contour_kwargs.update(regimes_contour_kwargs)

        if attractor_plot_type == 'glassbrain':
            default_attractor_kwargs = dict(display_mode='x', colorbar = False)
        elif attractor_plot_type == 'scatter':
            default_attractor_kwargs = dict()
        else:
            raise ValueError("Unknown attractor plot type.")
        default_attractor_kwargs.update(attractor_kwargs)

        if plot_type == 'scatter':
            default_kwargs = dict(alpha=1.0, s=10, linewidths=0, c='black')
        elif plot_type == 'hist2d':
            default_kwargs = dict(bins=100, cmap='gray_r')
        elif plot_type == 'density':
            default_kwargs = dict(cmap='gray_r')
        elif plot_type == 'contour':
            default_kwargs = dict(alpha=1, linewidths=0.1)
        elif plot_type == 'contourf':
            default_kwargs = dict(levels=20, antialiased=True, cmap='Greens')
        else:
            raise ValueError("Unknown type.")
        default_kwargs.update(kwargs)

        if ax is None:
            fig = plt.gcf()
            ax = fig.add_subplot(projection='polar')
            w, h = figaspect(1)
            ax.figure.set_size_inches(w, h)
        else:
            ax.set_aspect('equal')
            # todo: test if ax is specified

        max_r = 1
        for l, attractor in self.attractors.items():
            att = StandardScaler().fit_transform(np.array(attractor).reshape(1, -1).T).T
            att_cart = self.embedding_model.transform(np.tanh(att))[:, :2]
            r, th = _cart2pol(att_cart[:, 0], att_cart[:, 1])
            max_r = max(max_r, r.squeeze())
        ax.set_ylim([0, 1.1 * max_r])

        # plot actual data
        if activations is not None:
            # transform activations to embedding space
            activations = StandardScaler().fit_transform(activations.T).T
            embedded = self.embedding_model.transform(np.tanh(activations))
            r, th = _cart2pol(embedded[:, 0], embedded[:, 1])
            if plot_type == 'scatter':
                plot = ax.scatter(th, r, **default_kwargs)
                # produce a legend with a cross-section of sizes from the scatter
                if legend_kwargs is not None:
                    handles, labels = plot.legend_elements(prop="colors")
                    legend = ax.legend(handles, labels, **legend_kwargs)
            elif plot_type == 'hist2d':
                plot = ax.hist2d(th, r, **default_kwargs)
            elif plot_type == 'density' or plot_type == 'contour' or plot_type == 'contourf':
                H, x_edges, y_edges = np.histogram2d(embedded[:, 0], embedded[:, 1],
                                                     bins=density_bins,
                                                     density=True,
                                                     range=[[-max_r*1.2, max_r*1.2], [-max_r*1.2, max_r*1.2]])

                from scipy.ndimage import gaussian_filter
                H = gaussian_filter(H, sigma=density_sigma, mode='wrap')
                H[H<0.0001] = np.nan


                x, y = np.meshgrid(x_edges,
                                   y_edges)  # rectangular plot of polar data
                # calculate midpoints of bins
                y = (y[: -1, :-1] + y[1:, 1:]) / 2
                x = (x[: -1, :-1] + x[1:, 1:]) / 2
                rad, theta = _cart2pol(y, x)
                # fill
                if plot_type == 'density':
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        ax.pcolormesh(theta, rad, H, **default_kwargs)
                elif plot_type == 'contour':
                    ax.contour(theta, rad, H, **default_kwargs)
                elif plot_type == 'contourf':
                    ax.contourf(theta, rad, H, **default_kwargs)

            else:
                raise ValueError("Unknown type.")

        # plot attractor regimes
        ax.set_prop_cycle(None)
        def predict_label(x, y):
            return self.attractor_model.predict(np.array([x, y]).T.reshape(-1, self.attractor_model_dim))

        x, y = np.meshgrid(np.linspace(-max_r * 1.2, max_r * 1.2, 500),
                           np.linspace(-max_r * 1.2, max_r * 1.2, 500))  # rectangular plot of polar data
        pred = predict_label(x, y).reshape(x.shape)
        rad, theta = _cart2pol(x, y)

        # fill
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ax.pcolormesh(theta, rad, pred.T, **default_regimes_fill_kwargs)
        # contour
        ax.contour(theta, rad, pred.T, **default_regimes_contour_kwargs)

        # plot attractor states
        ax.set_prop_cycle(None)
        for l, attractor in self.attractors.items():
            att = StandardScaler().fit_transform(np.array(attractor).reshape(1, -1).T).T
            att_cart = self.embedding_model.transform(np.tanh(att))[:, :2]
            r, th = _cart2pol(att_cart[:, 0], att_cart[:, 1])
            if attractor_plot_type == 'scatter':
                ax.scatter(th, r, **default_attractor_kwargs)
            elif attractor_plot_type == 'glassbrain':
                trans = ax.transData.transform((th, r))
                trans = ax.figure.transFigure.inverted().transform(trans).flatten()
                network.State(attractor).plot(figure=ax.figure,
                                              axes=(trans[0] - 0.05, trans[1] - 0.05, 0.1, 0.1),
                                              **default_attractor_kwargs)
            else:
                raise ValueError("Unknown attractor_type.")

        ax.set_xticks([0, 0.5 * np.pi, np.pi, 1.5 * np.pi], ["PC1", "PC2", "", ""])
        ax.set_yticks(np.arange(0, np.round(max_r) + 1, 2))
        ax.set_rlabel_position(0)
        ax.tick_params(axis='y', colors='gray')
        ax.spines['polar'].set_visible(False)
        ax.xaxis.grid(True, linewidth=1, color='black')
        ax.yaxis.grid(True, linewidth=0.5, color='lightgrey')
        #ax.set_axisbelow('line')

        return ax


def simulate_activations(connectome, noise_coef=1, num_iter=1000, init_state=None,
                         progress=True, random_state=None, **kwargs):
    """
    Simulate activations of a Hopfield network  with a given connectome.
    Factory function for HopfieldSimulation dataclass.
    :param connectome: a 2D numpy array
    :param noise_coef:  noise coefficient
    :param num_iter: number of iterations
    :param init_state: initial state
    :param random_state: random state
    :param kwargs: additional arguments to network.Hopfield
    :return: HopfieldSimulation object
    """

    if not isinstance(connectome, np.ndarray) or connectome.ndim != 2 or connectome.shape[0] != connectome.shape[1]:
        raise ValueError("Connectome must be a 2D quadratic numpy array!")

    random = np.random.default_rng(random_state)

    default_kwargs = {
        "scale": True,
        "threshold": 0,
        "beta": 0.05
    }
    default_kwargs.update(kwargs)
    hopnet = network.Hopfield(connectome, **default_kwargs)

    states = np.zeros((num_iter + 1, hopnet.num_neuron))
    energies = np.zeros(num_iter)

    if init_state is None:
        states[0] = network.State(random.normal(0, 1, hopnet.num_neuron))
    else:
        states[0] = network.State(init_state)

    for i in tqdm(range(num_iter), disable=not progress):
        new_state, n_iter, energy = hopnet.update(states[i], num_iter=1)
        energies[i] = energy[-1]
        # add noise
        states[i + 1] = np.array(new_state) + random.normal(0, noise_coef, hopnet.num_neuron)

    return HopfieldSimulation(hopnet=hopnet, states=states[:-1], energies=energies)


def load_simulation(filename):
    """
    Load a serialized (pickled) HopfieldSimulation dataclass.
    :param filename:
    :return: HopfieldSimulation object
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)


def create_embeddings(simulation, attractor_sample=1000, num_hopfield_iter=100000, attractor_model_dim=2,
                      random_state=None, progress=True, **kwargs):
    """
    Construct a new Hopfield embeddings of a connectome from a HopfieldSimulation object.
    :param attractor_sample: ratio of states to be used for attractor model training
    :param simulation: HopfieldSimulation object
    :param kwargs: additional arguments to the embedding model (sklearn.decomposition.PCA)
    :return:
    """

    # PCA on simulated hopfield states
    pca = PCA(**kwargs)
    states = StandardScaler().fit_transform(simulation.states.T).T
    embedded = pca.fit_transform(np.tanh(states))

    # calculate attractor states for a subsample
    random = np.random.default_rng(random_state)

    attractors = dict()
    attractor_labels = np.zeros(min(int(simulation.states.shape[0]), attractor_sample), dtype=int)
    sample = random.choice(simulation.states.shape[0], min(int(simulation.states.shape[0]), attractor_sample),
                           replace=False)
    for i, s in tqdm(enumerate(sample), total=len(sample), disable=not progress):
        att, n_iter, energy = simulation.hopnet.update(simulation.states[s], num_iter=num_hopfield_iter)
        if n_iter == num_hopfield_iter:
            print(n_iter, '!!')
            raise RuntimeWarning("Convergence error!")

        if tuple(np.round(att, 6)) not in attractors.keys():
            attractors[tuple(np.round(att, 6))] = len(attractors)
            attractor_labels[i] = len(attractors) - 1
        else:
            attractor_labels[i] = attractors[tuple(np.round(att, 6))]

    # invert dictionary
    attractors = {v: np.array(k) for k, v in attractors.items()}

    # Fit a Multinomial Logistic Regression model that predicts the attractors on the first two PCs
    attractor_model = LogisticRegression(multi_class="multinomial")
    attractor_model.fit(embedded[sample, :attractor_model_dim], attractor_labels)

    return HopfiledEmbedding(hopnet=simulation.hopnet, embedding_model=pca,
                             attractors=attractors,
                             attractor_model=attractor_model,
                             attractor_model_dim=attractor_model_dim,
                             state_sample=simulation.states[sample],
                             attractor_sample=attractor_labels)


def load_embedding(filename):
    """
    Load a serialized (pickled) HopfieldEmbedding dataclass.
    :param filename: file to load
    :return: HopfieldEmbedding object
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)
