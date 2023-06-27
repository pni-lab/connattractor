from joblib import Parallel, delayed
import numpy as np
from nilearn import image
import nibabel as nib
import seaborn as sns
import matplotlib.pyplot as plt
from connattractor import network

def get_attractors_per_timesample(timeseries, hopnet, threshold=0):
    def workhorse(ts_i):
        activity = timeseries.loc[ts_i]
        fit = hopnet.update(activity, threshold=threshold, beta=hopnet.beta)
        attractor_state = np.array(fit[0])
        return attractor_state

    attractor_states = Parallel(n_jobs=-1)(delayed(workhorse)(i) for i in range(len(timeseries)))
    return attractor_states


def label_att_states(attractor_states, statedict, rtol=1e-05, atol=1e-08):
    # todo: not DRY, similar function count_unique_states existss
    ts_statelabels = np.zeros(len(attractor_states), dtype=int)
    for ts_i, attractor_state in enumerate(attractor_states):
        # store attractor state labels
        label = -1
        for dict_i, dictval in enumerate(statedict):
            if np.all(np.isclose(attractor_state, dictval, rtol=rtol,
                                 atol=atol)):  # or np.all(np.isclose(-1*attractor_state, dictval)):
                label = dict_i
                break
        if label < 0:
            statedict.append(attractor_state)
            label = len(statedict) - 1
        ts_statelabels[ts_i] = label
    return ts_statelabels, statedict


def mean_state_activation(statedict, statelabels, timeseries, standardize_act):
    # calculates average activation of each state over all timesamples
    # returns percentage of time spent in attractor and the att state
    meanact_sub = []
    for label, state in enumerate(statedict):

        time_spent_in_attractor = np.sum(statelabels == label)
        # time_spent_in_attractor = np.sum(statelabels == label) / len(statelabels)

        attractor_act = timeseries.loc[np.argwhere(statelabels == label).flatten()].mean()

        if standardize_act:
            attractor_act = (attractor_act - np.mean(attractor_act)) / np.std(attractor_act)

        meanact_sub.append((time_spent_in_attractor, attractor_act))
    return meanact_sub


import statsmodels.api as sm


class StatsModel:
    def __init__(self, model=None):
        if model is None:
            self.model = sm.OLS
        else:
            self.model = model

    def fit(self, Y, X):
        Y, X = self.drop_NaNs(Y, X)

        X = sm.add_constant(X)

        self.fit = self.model(Y, X).fit()

    def drop_NaNs(self, Y, X):
        X = X[~ np.isnan(Y)]
        Y = Y[~ np.isnan(Y)]
        return Y, X

    def get_pval(self):
        return self.fit.pvalues[1]

    def get_model_params(self):
        return self.fit.params[1]

    def get_t_stats(self):
        return abs(self.fit.tvalues[1])

    def get_r_squared(self):
        return np.round(self.fit.rsquared, decimals=3)


class StateDynamics:
    def __init__(self):
        self.mean_activation = dict()
        self.time_in_state = dict()
        return

    def read_meanactivation(self, meanacts, participants=None):
        self.n_states = len(meanacts)
        if participants is not None:
            self.participants = participants
        for sub_i, sub in enumerate(meanacts):
            for label, state in enumerate(sub):
                if label not in self.mean_activation.keys():
                    self.mean_activation[label] = dict()
                if label not in self.time_in_state.keys():
                    self.time_in_state[label] = dict()

                if participants is not None:
                    self.time_in_state[label][participants[sub_i]] = state[0]
                    self.mean_activation[label][participants[sub_i]] = state[1]
                else:
                    self.time_in_state[label][sub_i] = state[0]
                    self.mean_activation[label][sub_i] = state[1]

    def drop_subjects_w_missing_states(self):
        dropped_participants = []

        for state_key, state in self.mean_activation.items():
            for sub_key, sub in dict(state).items():
                if (np.isnan(sub).sum() > 0):
                    dropped_participants = state.pop(sub_key)
        if self.participants is not None:
            self.participants.pop(dropped_participants)
        return dropped_participants

    def _workhorse_perm(self, X, Y, rnd_seed=None):
        if rnd_seed is not None:
            np.random.seed(rnd_seed)
        np.random.shuffle(Y)
        perm_model = StatsModel()
        perm_model.fit(Y=Y, X=X)
        return perm_model.get_t_stats()

    def _workhorse_perm_regions(self, X, Y, rnd_seed=None):
        if rnd_seed is not None:
            np.random.seed(rnd_seed)
        np.random.shuffle(Y)
        n_regions = np.shape(X)[1]
        perm_region_t_stats = np.repeat(np.nan, n_regions)
        for region_i in range(n_regions):
            perm_model = StatsModel()
            perm_model.fit(Y=Y,
                           X=X[:, region_i])
            perm_region_t_stats[region_i] = perm_model.get_t_stats()
        return np.max(perm_region_t_stats)

    def perm_test_time_in_state(self, statelabel, target, permutations=1000, statsmodel=None, alpha=0.05):
        if isinstance(permutations, int):
            permutations = [np.random.randint(0, 1000000) for x in range(permutations)]

        ref_model = StatsModel(statsmodel)
        ref_model.fit(Y=np.copy(target),
                      X=np.fromiter(self.time_in_state[statelabel].values(), dtype=int))
        ref_t_stat = ref_model.get_t_stats()

        perm_t_stats = Parallel(n_jobs=-1)(delayed(self._workhorse_perm)(
            Y=np.copy(target),
            X=np.fromiter(self.time_in_state[statelabel].values(), dtype=int),
            rnd_seed=seed
        ) for seed in permutations)

        # time_stat_threshold = np.quantile(time_t_stats, q=1-alpha)
        return np.sum(perm_t_stats > ref_t_stat) / len(perm_t_stats)

    def perm_test_mean_activation_per_region(self, statelabel, target, permutations=1000, statsmodel=None, alpha=0.05):
        if isinstance(permutations, int):
            permutations = [np.random.randint(0, 1000000) for x in range(permutations)]

        n_regions = len(self.mean_activation[statelabel][list(self.mean_activation[statelabel].keys())[0]])
        sub_state_activations = np.zeros((len(self.participants), n_regions))
        for idx, sub_i in enumerate(self.mean_activation[statelabel]):
            sub_state_activations[idx, :] = self.mean_activation[statelabel][sub_i]

        ref_region_t_stats = np.zeros(n_regions)
        for region_i in range(n_regions):
            ref_model = StatsModel(statsmodel)
            ref_model.fit(Y=np.copy(target),
                          X=np.copy(sub_state_activations[:, region_i]))
            ref_region_t_stats[region_i] = ref_model.get_t_stats()

        perm_t_stats = Parallel(n_jobs=-1)(delayed(self._workhorse_perm_regions)(
            Y=np.copy(target),
            X=sub_state_activations,
            rnd_seed=seed
        ) for seed in permutations)

        fwer_threshold = np.quantile(perm_t_stats, q=1 - alpha)
        alpha_regions = np.where(np.abs(ref_region_t_stats) > fwer_threshold)

        for reg in alpha_regions:
            sns.regplot(x=target,
                        y=sub_state_activations[:, reg])

        network.State(ref_region_t_stats).plot(smooth=0, threshold=fwer_threshold)
        plt.show()

        return np.sum(perm_t_stats > np.max(ref_region_t_stats)) / len(perm_t_stats), alpha_regions