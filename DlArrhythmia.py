import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/"
DATASETS = ["arrhythmia.data"]
DATASET_PATH = "datasets/arrhythmia/"
DATASET_INDEX = ["age,sex,height,weight,QRS duration,P-R interval,Q-T interval,T interval,P interval,QRS,T,P,QRST,J,Heart rate"]
INDEX_PER_CHANNEL1 = ["Q wave","R wave","S wave","R'wave","S' wave","#intrinsic deflections","ragged R wave","diphasic derivation of R wave","ragged P wave","diphasic derivation of P wave","ragged T wave","diphasic derivation of T wave"]
INDEX_PER_CHANNEL2 = ["JJ wave","Q wave","R wave","S wave","R' wave","S' wave","P wave","T wave","QRSA","QRSTA"]
CHANNEL_NAME = ["D1","D2","D3","AVR","AVL","AVF","V1","V2","V3","V4","V5","V6"]
PREDICTION_INDEX = "Arrhythmia Type"

def fetch_data(dataset_path=DATASET_PATH):
    if not os.path.isdir(dataset_path):
        os.makedirs(dataset_path)
    for file in DATASETS:
        urllib.request.urlretrieve(DOWNLOAD_ROOT+file, dataset_path+file+'.temp')
        with open(dataset_path+file+'.temp', 'r') as original:
            data = original.read()
            data = data.replace("?","")
        with open(dataset_path+file, 'w') as modified:
            modified.write(DATASET_INDEX[0])
            for channel in CHANNEL_NAME:
                for idx1 in INDEX_PER_CHANNEL1:
                    modified.write(","+channel+"_"+idx1)
            for channel in CHANNEL_NAME:
                for idx2 in INDEX_PER_CHANNEL2:
                    modified.write(","+channel+"_"+idx2)
            modified.write(","+PREDICTION_INDEX+"\n"+data)
        os.remove(dataset_path+file+'.temp')

if __name__ == '__main__':
    fetch_data()