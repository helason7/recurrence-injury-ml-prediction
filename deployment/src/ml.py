import pandas as pd
import numpy as np
import streamlit as st
import joblib
import datetime
import os

BASE_DIR = os.path.dirname(__file__)  # Lokasi file .py
file_path = os.path.join(BASE_DIR, 'basketInjModelV1.pkl')

# Load pipeline dari file
basket_model = joblib.load(file_path)

def run():
    
  # pembuatan form
  with st.form(key='Predict the player'):
    st.markdown('===Data Profil Pemain===')
    name = st.text_input('Nama Pemain', value='Masukan Nama Pemain')
    age = st.number_input('Umur Pemain', min_value=16, max_value=50, value=20, step=1)
    weight = st.number_input('Berat Badan Pemain', min_value=60, max_value=120, value=75, step=1, help='Dalam Kg')
    height = st.slider('Tinggi Badan Pemain', min_value=150, max_value=220, value=175, step=1, help='Dalam cm')
    position = st.selectbox('Posisi Pemain', ('Center', 'Guard', 'Foward'), index=0)

    st.markdown('===Data Cedera Pemain===')
    tipe = st.selectbox('Tipe Cedera', ('ACL Tear', 'Ankle Sprain', 'Knee Injury', 'Shoulder Dislocation', 'Hamstring Strain'), index=0)
    tingkat = st.selectbox('Tingkat Cedera', ('Mild', 'Moderate', 'Severa'), index=0)
    tanggal = st.date_input(
        "Pilih tanggal:",
        value=datetime.date.today()
    )
    st.markdown('===Data Rehabilitasi Pemain===')
    program = st.radio('Program Rehabilitasi yg dilakukan', 
            ('Physiotherapy', 'Flexibility Exercises', 'Strength Training',
                'Balance Training'), index=2)
    duration = st.slider('Durasi Rehabilitasi', min_value=0, max_value=14, value=2, step=1, help='Berapa Minggu')
    # recurrence = st.radio('Kembali Kambuh', ('Ya', 'Tidak'))
    score = st.slider('Hasil Rehabilitasi', min_value=0, max_value=100, value=2, step=1, help='Persentase')

    st.markdown('===Data Gerak Biomekanik Pemain===')
    knee = st.number_input('Sudut Lutut', min_value=30.00, max_value=100.00, value=40.00, help='derajat / degree')
    jump = st.number_input('Tinggi Lompatan Maksimal', min_value=30.00, max_value=100.00, value=40.00, help='cm')
    flex = st.number_input('Sudut Fleksibelitas Ankle', min_value=30.00, max_value=100.00, value=40.00, help='derajat / degree')
    speed = st.number_input('Kecepatan Gerak', min_value=30.00, max_value=100.00, value=40.00, help='ms')
    reflex = st.number_input('Kecepatan Reflek', min_value=30.00, max_value=100.00, value=40.00, help='ms')

    score = score / 100
    
    submiteed = st.form_submit_button('Predict')

    data_inf = {
        'Player ID': 9999,
        'Umur': age,
        'Tinggi': height,
        'Berat': weight,
        'Posisi': position,
        'Tipe Cedera': tipe,
        'Tingkat Cedera': tingkat,
        'Program Rehab': program,
        'Tanggal Cedera': tanggal,
        'Durasi Rehab (dalam minggu)': duration,
        'Rehabilitasi Skor': score,
        'Sudut Lutut': knee,
        'Tinggi Lompatan':jump,
        'Sudut Fleksibel Angkle': flex,
        'Kecepatan Gerak': speed,
        'Kecepatan Reflek': reflex
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submiteed:
        y_pred_inf = basket_model.predict(data_inf)
        if y_pred_inf == 1:
            hasil = 'Ada potensi terjadinya Kambuh Cedera. Periksa kembali hasil Rehabilitasi dan Gerak Biomekanik'
        else:
            hasil = 'Tidak ada potensi terjadinya Kambuh Cedera. Selamat Pemain Dapat kembali bermain' 
        st.write('# ', hasil)
        

if __name__ == '__main__':
  run()