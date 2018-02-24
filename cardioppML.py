import os
import json

import pandas as pd
import simplejson
from flask import Flask, render_template, request
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


def load_dataset(dataset_path):
    dataset_path = os.path.join(app.root_path, dataset_path)
    return pd.read_csv(dataset_path)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    if not len(data) == 80:
        return "please provide 80 params. Your data only "+str(len(data))
    data = np.reshape(data,(1,-1))
    prediction = forest_reg.predict(data)
    return str(prediction)


if __name__ == '__main__':
    arrhythmia = load_dataset("prod-datasets/arrhythmia/simplified.arrhythmia_train.data")
    del arrhythmia["Unnamed: 0"]
    arrhythmia_arr = arrhythmia.values
    arrhythmia_label = arrhythmia_arr[:, 80]
    arrhythmia_train = np.delete(arrhythmia_arr, 80, 1)
    forest_reg = RandomForestRegressor()
    forest_reg.fit(arrhythmia_train, arrhythmia_label)
    app.run()
