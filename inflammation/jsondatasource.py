import glob
import os

from inflammation import models

class JSONDataSource:
    """
    Loads all the inflammation JSON's within a specified folder.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation JSON's found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)
