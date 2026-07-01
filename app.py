import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("zoo_model(gini).pkl")

st.title("🦁 Zoo Animal Prediction")

st.write("Enter the animal features below.")

hair = st.selectbox("Hair", [0, 1])
feathers = st.selectbox("Feathers", [0, 1])
eggs = st.selectbox("Eggs", [0, 1])
milk = st.selectbox("Milk", [0, 1])
airborne = st.selectbox("Airborne", [0, 1])
aquatic = st.selectbox("Aquatic", [0, 1])
predator = st.selectbox("Predator", [0, 1])
toothed = st.selectbox("Toothed", [0, 1])
backbone = st.selectbox("Backbone", [0, 1])
breathes = st.selectbox("Breathes", [0, 1])
venomous = st.selectbox("Venomous", [0, 1])
fins = st.selectbox("Fins", [0, 1])

legs = st.number_input(
    "Number of Legs",
    min_value=0,
    max_value=8,
    step=1
)

tail = st.selectbox("Tail", [0, 1])
domestic = st.selectbox("Domestic", [0, 1])
catsize = st.selectbox("Cat Size", [0, 1])

if st.button("Predict"):

    data = np.array([[hair,
                      feathers,
                      eggs,
                      milk,
                      airborne,
                      aquatic,
                      predator,
                      toothed,
                      backbone,
                      breathes,
                      venomous,
                      fins,
                      legs,
                      tail,
                      domestic,
                      catsize]])

    prediction = model.predict(data)

    st.success(f"Predicted Class Type : {prediction[0]}")