import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/"
DATASETS = ["processed.hungarian.data","processed.switzerland.data"]
DATASET_PATH = "datasets/heart-disease/"
DATASET_INDEX = ["age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,num"]

def fetch_data(dataset_path=DATASET_PATH):
    if not os.path.isdir(dataset_path):
        os.makedirs(dataset_path)
    for file in DATASETS:
        urllib.request.urlretrieve(DOWNLOAD_ROOT+file, dataset_path+file+'.temp')
        with open(dataset_path+file+'.temp', 'r') as original:
            data = original.read()
            data = data.replace("?","")
        with open(dataset_path+file, 'w') as modified: modified.write(DATASET_INDEX[0]+'\n'+ data)
        os.remove(dataset_path+file+'.temp')

if __name__ == '__main__':
    fetch_data()