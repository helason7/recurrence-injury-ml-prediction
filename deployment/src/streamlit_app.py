import streamlit as st
import eda 
import ml as pred

st.set_page_config(
    page_title='Basketball Injury',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Choses Page:', ('EDA', 'ML Prediksi Cedera Pemain'))

if page == 'EDA':
    eda.run()
else:
    pred.run()