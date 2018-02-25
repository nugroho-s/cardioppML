import os

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Imputer

app = Flask(__name__)

sugestion = ['[{"Penyakit":"normal"}]',
             '[{"Penyakit":"Coronary Artery Disease","Saran":"Aktivitas aerobik selama 20-30 menit, 5 hari seminggu. Berhenti merokok tembakau. Mengurangi asupan makanan tinggi lemak seperti susu, minyak, dan daging merah"},{"Spesialis":"Kardiolog,Ahli bedah kardiotoraks,Penyedia perawatan primer (PCP),Dokter pengobatan darurat"}]',
             '[{"Penyakit":"Old Anterior Myocardial Infarction"},{"Spesialis":"Kardiolog"}]',
             '[{"Penyakit":"Old Inferior Myocardial Infarction"},{"Spesialis":"Kardiolog"}]',
             '[{"Penyakit":"Sinus Tachycardia"},{"Saran":"Menghindari hal yang mengakibatkan denyut jantung meningkat,seperti stimulan atau kegiatan yang memicu stress. mengonsumsi makanan untuk diet jantung. berolahraga. menjaga berat tubuh"}]',
             '[{"Penyakit":"Sinus Bradycardia"},{"Saran":"Berolahraga,diet,menjaga berat badan,menjaga tekanan darah dan kolesterol,hindari rokok dan obat terlarang"}]',
             '[{"Penyakit":"Ventricular Premature Contraction"},{"Saran":{"Penghindaran rangsangan yang membuat jantung berdebar, menghindari stress"}}]',
             '[{"Penyakit":"Supraventricular Premature Contraction"},{"Saran":"Menghindari rokok, kafein dan minuman keras"}]',
             '[{"Penyakit":"Left bundle branch block"},{"Saran":"Mengobati kondisi yang mendasari,pemantauan berlanjut"}]'
             '[{"Penyakit":"Right bundle branch block"},{"Saran":"Mengobati kondisi yang mendasari,pemantauan berlanjut"}]',
             '[{"Penyakit":"First degree AtrioVentricular block"},{"Saran":"Konsultasi ke dokter, pengamatan ecg secara rutin"}]',
             '[{"Penyakit":"Second degree AtrioVentricular block"},{"Saran":"Konsultasi ke dokter, pengamatan ecg secara rutin"}]',
             '[{"Penyakit":"Third degree AtrioVentricular block"},{"Saran":"Konsultasi ke dokter, pengamatan ecg secara rutin"}]',
             '[{"Penyakit":"Left Ventricular Hypertrophy"},{"Saran":"Berobat ke dokter jantung, menarapkan gaya hidup sehat"}]',
             '[{"Penyakit":"Atrial Fibrillation or Flutter"},{"Saran":"Berobat ke dokter jantung dan meminum obat secara rutin. mengonsumsi walfirin/aspirin"}]',
             '[{"Penyakit":"Penyakit lain"},{"Saran":"Berkonsultasi ke dokter jantung dan menunjukkan hasil ecg pada ponsel"}]'
             ]


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
    prediction = forest_cls.predict(imp.transform(data))
    idx = int(prediction)
    return sugestion[idx-1]


if __name__ == '__main__':
    arrhythmia = load_dataset("prod-datasets/arrhythmia/simplified.arrhythmia_train.data")
    del arrhythmia["Unnamed: 0"]
    arrhythmia_arr = arrhythmia.values
    arrhythmia_label = arrhythmia_arr[:, 80]
    arrhythmia_train = np.delete(arrhythmia_arr, 80, 1)
    # Create our imputer to replace missing values with the mean e.g.
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp = imp.fit(arrhythmia_train)
    forest_cls = RandomForestClassifier()
    forest_cls.fit(arrhythmia_train, arrhythmia_label)
    app.run()
