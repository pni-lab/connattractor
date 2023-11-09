from importlib import resources
from pathlib import Path
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def get_base_path():
    return resources.files('resources')
def get_MIST_nii_path():
    base_path = get_base_path()
    return Path.joinpath(base_path, 'MIST122_relabeled.nii.gz')

def get_MIST_labels_path():
    base_path = get_base_path()
    return Path.joinpath(base_path, 'MIST122_relabeled.tsv')

def get_fcHNN_embedding():
    base_path = get_base_path()
    target_path = Path.joinpath(base_path, 'default_hopfield_embedding_0.37.pkl')

    with open(target_path, 'rb') as f:
        embedding = pickle.load(f)

    return embedding

def get_ex_connectome():
    base_path = get_base_path()
    target_path = Path.joinpath(base_path, 'connectome_partial_correlation.csv')

    mtx = pd.read_csv(target_path)
    mtx = mtx.drop("Unnamed: 0", axis='columns')
    mtx = mtx.drop("GlobSig", axis="columns")
    mtx = mtx.drop(0, axis="index")

    return mtx

def get_ex_task_data():
    base_path = get_base_path()
    _fd_thr = 0.15
    _perc_scrub_thr = 0.5

    rest = np.repeat(np.nan, 122)
    task = np.repeat(np.nan, 122)
    temperatures = [np.nan]
    sub_rest = [np.nan]
    sub_task = [np.nan]

    _TR_ = 2.0  # seconds

    for sub in range(1, 33):
        sub_pad = f'{sub + 1:02}'

        fd_path = Path.joinpath(base_path, Path('ex_timeseries_task/sub-' + sub_pad + '_FD.txt'))
        fd = pd.read_csv(fd_path).values.flatten()
        fd = np.hstack(([0], fd))

        ts_path = Path.joinpath(base_path, Path('ex_timeseries_task/sub-' + sub_pad + '_ts.txt'))
        ts = pd.read_csv(ts_path, sep='\t').iloc[:, 1:].values

        events_path = Path.joinpath(base_path, Path('ex_timeseries_task/sub-' + sub_pad + '_task-heatpainwithregulationandratings_run-01_events.tsv'))
        events = pd.read_csv(events_path, sep='\t')

        ts = StandardScaler().fit_transform(ts)

        if np.sum(fd > _fd_thr) / len(fd) < _perc_scrub_thr:
            ts[fd >= _fd_thr] = np.nan
        else:
            ts[:] = np.nan
            print('perc. scrubbed:', np.sum(fd > _fd_thr) / len(fd))

        # task timeframes: same duration, 6 sec delay in onset due to HRF
        # rest timeframes: starts 6 sec after last block, right until the onset of the next block

        rest_block = ts[0:(int(np.round(18 + 2 / _TR_))), :]
        rest = np.vstack((rest, rest_block))
        sub_rest += [sub] * rest_block.shape[0]

        for i in events.index:

            onset = int(np.round(events.loc[i, "onset"] / _TR_))
            end = onset + int(np.round(events.loc[i, "duration"] / _TR_))

            if not np.isnan(events.loc[i, "temperature"]):
                # early phase
                current_block = ts[(onset + int(np.round(8 / _TR_))):(onset + int(np.round(16 / _TR_))), :]
                task = np.vstack((task, current_block))
                temperatures += [events.loc[i, "temperature"]] * current_block.shape[0]
                sub_task += [sub] * current_block.shape[0]

    temperatures = np.array(temperatures)[~np.ma.fix_invalid(task).mask.any(axis=1)]
    sub_rest = np.array(sub_rest)[~np.ma.fix_invalid(rest).mask.any(axis=1)]
    sub_task = np.array(sub_task)[~np.ma.fix_invalid(task).mask.any(axis=1)]
    task = task[~np.ma.fix_invalid(task).mask.any(axis=1)]
    rest = rest[~np.ma.fix_invalid(rest).mask.any(axis=1)]
    return rest, sub_rest, task, sub_task
