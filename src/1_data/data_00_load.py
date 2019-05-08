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
# %%
class AIDataSet():
    def __init__(self, image_folder, image_extension, df, col_file, col_target):
        """

        :param image_folder:
        :param image_extension:
        :param df:
        :param col_target:
        """
        self.image_folder = image_folder
        self.image_extension = image_extension
        self.df = df
        self.col_file = col_file
        self.target_col = col_target

        logging.debug("{} images found".format(len(self.list_images())))
        logging.info("Dataframe with {} records, target column is {}".format(len(df), self.target_col))

    def list_images(self):
        image_list = self.image_folder.glob("*"+self.image_extension)
        return list(image_list)

# %%
image_folder = path_data / "images"
ds = AIDataSet(image_folder, ".jpg", df, 'class')
res = ds.list_images()


image_folder.glob("*."+self.image_extension)
