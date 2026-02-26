import streamlit as st
import joblib
import numpy as np

# Load model yang sudah dibuat di Colab
model = joblib.load('model_iris.pkl')

st.title("Prediksi Bunga Iris")

# Input dari pengguna
s_length = st.number_input("Sepal Length", 0.0, 10.0)
s_width = st.number_input("Sepal Width", 0.0, 10.0)
p_length = st.number_input("Petal Length", 0.0, 10.0)
p_width = st.number_input("Petal Width", 0.0, 10.0)

if st.button("Prediksi"):
    data = np.array([[s_length, s_width, p_length, p_width]])
    prediksi = model.predict(data)
    nama_bunga = le.inverse_transform(prediksi)
    st.success(f"Hasilnya adalah: {nama_bunga[0]}")
