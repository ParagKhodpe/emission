import streamlit as st
import joblib

# Load the model
model = joblib.load('co2_model.pkl')

st.title('CO2 Emissions Prediction')

# Input features
engine_size = st.number_input('Engine Size (L)')
cylinders = st.number_input('Number of Cylinders')
fuel_consumption_city = st.number_input('Fuel Consumption City (L/100km)')
fuel_consumption_hwy = st.number_input('Fuel Consumption Highway (L/100km)')

# Make prediction
features = [engine_size, cylinders, fuel_consumption_city, fuel_consumption_hwy]
if st.button('Predict'):
    prediction = model.predict([features])
    st.write(f'Predicted CO2 Emissions: {prediction[0]} g/km')
