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


path_labels = PATH_DATA_ROOT / "annotations" / "list.txt"
assert path_labels.exists()

df = pd.read_csv(path_labels, header=6, delim_whitespace=True)
df.columns = ['file name', 'class', 'species', 'breed']
df.head()
#%%
class AIDataSet():
    def __init__(self, image_folder, df, target_col):
        """

        :param image_folder:
        :param df:
        :param target_col:
        """
        self.image_folder = image_folder
        self.df = df
        self.target_col = target_col
        
