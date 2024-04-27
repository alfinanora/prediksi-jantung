from flask import Flask, render_template, request
import pickle
import os
import pandas as pd  

app = Flask(__name__)

# Inisialisasi model
model = pickle.load(open('./models/knn_model.pkl', 'rb'))
scaler = pickle.load(open('./models/scaler.pkl', 'rb'))
pos = pickle.load(open('./models/pos.pkl', 'rb'))

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dataset')
def dataset():
    # Menentukan path lengkap file heart.csv
    csv_heart_path = os.path.join('heart_failure.csv')

    # Membaca dataset heart.csv
    df_heart = pd.read_csv(csv_heart_path)

    return render_template('dataset.html', df_heart=df_heart)

@app.route('/pengujian')
def pengujian():
    return render_template('pengujian.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            form_values = request.form.to_dict()

            data = {}

            data = {key: [float(value)] if value.replace('.', '', 1).isdigit() else value for key, value in form_values.items()}

            # Membuat data kedalam bentuk dataframe
            df = pd.DataFrame(data)

            # Seleksi fitur PSO
            selected_features = df.columns[pos > 0.5]
            new_data_selected = df[selected_features]

            # Scaler
            new_data_std = scaler.transform(new_data_selected)

            # Prediksi hasil
            prediction = model.predict(new_data_std)
            predicted_class = prediction[0]

            # Return prediction as JSON
            return str(predicted_class)

        except Exception as e:
            return {"error": str(e)}

@app.route('/conmat')
def conmat():
    return render_template('conmat.html')

if __name__ == '__main__':
    app.run(debug=True)