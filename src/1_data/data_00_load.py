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
        self.col_target = col_target

        logging.info("{} images found".format(len(self.list_images())))
        logging.info("Dataframe with {} records, target column is {}".format(len(df), self.col_target))
        self.check_alignment(strict=False)
    def list_images(self):
        image_list = self.image_folder.glob("*"+self.image_extension)
        return list(image_list)

    def check_alignment(self, strict):
        # Get the file names from the image folder
        image_names = [p.stem for p in self.list_images()]
        # Compare the number of images in the dataframe to the images in folder
        extra_df_records = self.df[self.df['file name'].isin(image_names) == False]
        logging.info("{} extra images in the dataframe".format(len(extra_df_records)))

        # Compare the number of images in the folder to the dataframe labels
        extra_folder_images = pd.Series(image_names)[pd.Series(image_names).isin(df['file name']) == False]
        logging.info("{} extra images found in the folder".format(len(extra_folder_images)))
        if strict:
            assert extra_df_records == 0
            assert extra_folder_images == 0

# %%
image_folder = path_data / "images"
ds = AIDataSet(image_folder, ".jpg", df, 'file name', 'class')
df.head()
col_target = 'species'
df.groupby(col_target).count()

