# Importing essential libraries
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS
import os
import pandas as pd  

# Inisialisasi objek Flask
app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def dashboard():
    return render_template('dashboard.html', css_file='css/styles.min.css')

@app.route('/dataset')
def dataset():
    # Menentukan path lengkap file heart.csv
    csv_heart_path = os.path.join('heart_failure.csv')

    # Membaca dataset heart.csv
    df_heart = pd.read_csv(csv_heart_path)

    return render_template('dataset.html', df_heart=df_heart,  css_file='css/styles.min.css')


@app.route('/pengujian')
def pengujian():
    return render_template('pengujian.html', css_file='css/styles.min.css')

@app.route('/conmat')
def conmat():
    return render_template('conmat.html', css_file='css/styles.min.css')

if __name__ == '__main__':
    app.run(debug=True)