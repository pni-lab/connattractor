# config.py

import os
import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

MIST122_NII = os.path.join(ROOT_DIR, '../data_in/MIST122_relabeled.nii.gz')
MIST122_LABELS_TSV = os.path.join(ROOT_DIR, '../data_in/MIST122_relabeled.tsv')

HCP_ICA_PMAP_50 = os.path.join('/home/renglert/Data/HCP/HCP1200_Parcellation_Timeseries_Netmats_recon2/HCP_PTN1200_recon2/groupICA/groupICA_3T_HCP1200_MSMAll_d50.ica/melodic_IC_sum.nii.gz')

DEFAULT_ATLAS_NII = MIST122_NII
DEFAULT_ATLAS_LABELS_TSV = MIST122_LABELS_TSV
DEAFULT_ATLAS_M = 122

EX_TIMESERIES = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/bochum-*.tsv"))
EX_FD = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/FD*"))

EX_TIMESERIES_LOW_PAIN_SENS = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/bochum-*low.tsv"))
EX_FD_LOW_PAIN_SENS = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/FD*low*"))

EX_TIMESERIES_HIGH_PAIN_SENS = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/bochum-*high.tsv"))
EX_FD_HIGH_PAIN_SENS = glob.glob(os.path.join(ROOT_DIR, "../data_in/ex_timeseries/FD*high*"))


