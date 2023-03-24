import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_anemia.sav', 'rb'))

# judul web
st.title('Prediksi Anemia')

Gender = st.number_input('Jenis Kelamin')

Hemoglobin = st.number_input('Hemoglobin')

MCH = st.number_input('MCH')

MCHC = st.number_input('MCHC')

MCV = st.number_input('MCV')

# code for prediction
anemia_diagnosis = ''

if st.button ('Prediksi Penyakit Anemia') :
    anemia_prediction = model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])
    
    if (anemia_prediction[0]==1):
        anemia_diagnosis = ' Mengidap'
    else:
        anemia_diagnosis = 'tidak mengidap'
        
st.success(anemia_diagnosis)
st.text('Andrian Herbert Parsaoran Sitohang - 201351150 - Malam A')