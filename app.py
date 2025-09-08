
# app.py
import streamlit as st
import pickle
import numpy as np

# Load the model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Iris Flower Prediction")

# Input fields
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.35)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.3)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    species = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"Predicted Species: {species[prediction]}")
