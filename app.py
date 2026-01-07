import streamlit as st
import pandas as pd
import pickle

st.title("🏥 Insurance Cost Prediction")

# Load model
with open("insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.subheader("Enter Details")

age = st.number_input("Age", min_value=1, step=1)
bmi = st.number_input("BMI", min_value=10.0, step=0.1)
children = st.number_input("Children", min_value=0, step=1)

if st.button("Predict Insurance Cost"):
    input_data = pd.DataFrame(
        [[age, bmi, children]],
        columns=["age", "bmi", "children"]
    )
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:.2f}")
