#%%
# Load data
#

#%% ===========================================================================
# Data source and paths
# =============================================================================
path_data = Path(PATH_DATA_ROOT, r"").expanduser()
assert path_data.exists(), "Data path does not exist: {}".format(path_data)
logging.info("Data path {}".format(PATH_DATA_ROOT))

#%% ===========================================================================
# Load data
# =============================================================================
logging.info(f"Loading files into memory")


