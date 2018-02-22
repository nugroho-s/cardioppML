import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/"
DATASETS = ["hungarian.data","switzerland.data"]
DATASET_PATH = "datasets/heart-disease/"

def fetch_data(dataset_path=DATASET_PATH):
    if not os.path.isdir(dataset_path):
        os.makedirs(dataset_path)
    for file in DATASETS:
        urllib.request.urlretrieve(DOWNLOAD_ROOT+file, dataset_path+file)

if __name__ == '__main__':
    fetch_data()