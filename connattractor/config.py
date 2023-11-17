# config.py

import os
from connattractor import utils

import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

MIST122_NII = utils.get_MIST_nii_path()
MIST122_LABELS_TSV = utils.get_MIST_labels_path()

DEFAULT_ATLAS_NII = MIST122_NII
DEFAULT_ATLAS_LABELS_TSV = MIST122_LABELS_TSV
DEAFULT_ATLAS_M = 122
