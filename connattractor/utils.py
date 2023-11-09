from importlib import resources
from pathlib import Path
import pandas as pd
import pickle
def get_fcHNN_embedding():
    base_path = resources.files('resources')
    target_path = Path.joinpath(base_path, 'default_hopfield_embedding_0.37.pkl')

    with open(target_path, 'rb') as f:
        embedding = pickle.load(f)

    return embedding

def get_ex_connectome():
    base_path = resources.files('resources')

    target_path = Path.joinpath(base_path, 'connectome_partial_correlation.csv')

    mtx = pd.read_csv(target_path)
    mtx = mtx.drop("Unnamed: 0", axis='columns')
    mtx = mtx.drop("GlobSig", axis="columns")
    mtx = mtx.drop(0, axis="index")

    return mtx
