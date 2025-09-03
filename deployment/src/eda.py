import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import os

BASE_DIR = os.path.dirname(__file__)  # Lokasi file .py
file_path = os.path.join(BASE_DIR, "dataset.csv")

# df = pd.read_csv(file_path)
def run():
    st.title("Aplikasi Prediksi Potensi Kambuh Cedera Pada Pemain Basket Pasca Rehabilitasi")
    st.subheader('Explorasi Data Analis')
    gambar = Image.open('./src/basketball knee.jpg')
    st.write(gambar, caption='caption gambar')
    data = pd.read_csv(file_path)
    st.dataframe(data)
    st.write('### Tipe Cedera Pada Kebanyakan Pemain Basket')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Tipe Cedera', data=data)
    st.pyplot(fig)

        # membuat plotly plot
    st.write('### Potlyplot - Posisi Pemain vs Umur ')
    fig = px.scatter(data, x='Posisi Pemain', y='Umur Pemain', hover_data=['Posisi Pemain', 'Umur Pemain'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()