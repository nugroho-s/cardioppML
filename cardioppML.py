import os

import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def load_dataset(dataset_path):
    dataset_path = os.path.join(app.root_path, dataset_path)
    return pd.read_csv(dataset_path)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/coba')
def coba():
    hungarian_data = load_dataset("datasets/heart-disease/hungarian.data")
    hungarian_data.head()
    return hungarian_data.to_json(orient='values')


if __name__ == '__main__':
    app.run()
