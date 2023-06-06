# config.py

import os
import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

MIST122_NII = os.path.join(ROOT_DIR, '../data_in/MIST122_relabeled.nii.gz')
MIST122_LABELS_TSV = os.path.join(ROOT_DIR, '../data_in/MIST122_relabeled.tsv')

DEFAULT_ATLAS_NII = MIST122_NII
DEFAULT_ATLAS_LABELS_TSV = MIST122_LABELS_TSV
DEAFULT_ATLAS_M = 122
