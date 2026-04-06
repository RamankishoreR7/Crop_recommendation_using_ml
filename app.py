import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load('crop_model.joblib')

st.title("Crop Recommendation System 🌾")

st.write("""
Enter the values for the soil and weather parameters below, and get a crop recommendation!
""")

# Input fields for features
N = st.number_input('Nitrogen content in soil (N)', min_value=0, max_value=140, value=90)
P = st.number_input('Phosphorus content in soil (P)', min_value=0, max_value=140, value=42)
K = st.number_input('Potassium content in soil (K)', min_value=0, max_value=205, value=43)
temperature = st.number_input('Temperature (°C)', min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=80.0)
ph = st.number_input('Soil pH value', min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=300.0, value=120.0)

if st.button('Predict Crop'):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"Recommended Crop: **{prediction[0].capitalize()}**")
