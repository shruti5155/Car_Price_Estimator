import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model (already includes preprocessing pipeline)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car.csv')

st.title("Car Price Estimator")
st.markdown("This app predicts the price of a car you want to sell. Fill the details below:")

# Dropdowns
company = st.selectbox("Select the Company", sorted(car['company'].unique()))
car_models = sorted(car[car['company'] == company]['name'].unique())
car_model = st.selectbox("Select the Model", car_models)

year = st.selectbox("Select Year of Purchase", sorted(car['year'].unique(), reverse=True))
fuel_type = st.selectbox("Select Fuel Type", car['fuel_type'].unique())
kms_driven = st.number_input("Enter the Number of Kilometres the car has travelled", step=1000)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Car Price: ₹ {np.round(prediction, 2)}")