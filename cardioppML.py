import os
import json

import pandas as pd
import simplejson
from flask import Flask, render_template
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


def load_dataset(dataset_path):
    dataset_path = os.path.join(app.root_path, dataset_path)
    return pd.read_csv(dataset_path)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/coba')
def coba():
    some_data = arrhythmia_train[:5]
    some_label = arrhythmia_label[:5]
    prediction = lin_reg.predict(some_data)
    # for i in range(len(prediction)):
    #     print("pred:"+str(prediction[i]))
    x = prediction.astype(str)
    print(x)
    return simplejson.dumps(x.tolist())


if __name__ == '__main__':
    arrhythmia = load_dataset("prod-datasets/arrhythmia/processed.arrhythmia_train.data")
    arrhythmia_arr = arrhythmia.values
    arrhythmia_label = arrhythmia_arr[:, 279]
    arrhythmia_train = np.delete(arrhythmia_arr, 279, 1)
    lin_reg = LinearRegression()
    lin_reg.fit(arrhythmia_train, arrhythmia_label)
    app.run()
