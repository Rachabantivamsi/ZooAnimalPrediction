import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("zoo_model(gini).pkl")

# Convert Yes/No to 1/0
yes_no = {
    "Yes": 1,
    "No": 0
}

# Class labels
class_names = {
    1: "🐘 Mammal",
    2: "🐦 Bird",
    3: "🐍 Reptile",
    4: "🐟 Fish",
    5: "🐸 Amphibian",
    6: "🐞 Bug",
    7: "🦑 Invertebrate"
}

# Title
st.title("🦁 Zoo Animal Prediction")
st.write("Select the animal characteristics below and click Predict.")

# Inputs
hair = st.selectbox("Hair", ["Yes", "No"])
feathers = st.selectbox("Feathers", ["Yes", "No"])
eggs = st.selectbox("Eggs", ["Yes", "No"])
milk = st.selectbox("Milk", ["Yes", "No"])
airborne = st.selectbox("Airborne", ["Yes", "No"])
aquatic = st.selectbox("Aquatic", ["Yes", "No"])
predator = st.selectbox("Predator", ["Yes", "No"])
toothed = st.selectbox("Toothed", ["Yes", "No"])
backbone = st.selectbox("Backbone", ["Yes", "No"])
breathes = st.selectbox("Breathes", ["Yes", "No"])
venomous = st.selectbox("Venomous", ["Yes", "No"])
fins = st.selectbox("Fins", ["Yes", "No"])

legs = st.number_input(
    "Number of Legs",
    min_value=0,
    max_value=8,
    step=1
)

tail = st.selectbox("Tail", ["Yes", "No"])
domestic = st.selectbox("Domestic", ["Yes", "No"])
catsize = st.selectbox("Cat Size", ["Yes", "No"])

# Predict Button
if st.button("Predict"):

    data = np.array([[
        yes_no[hair],
        yes_no[feathers],
        yes_no[eggs],
        yes_no[milk],
        yes_no[airborne],
        yes_no[aquatic],
        yes_no[predator],
        yes_no[toothed],
        yes_no[backbone],
        yes_no[breathes],
        yes_no[venomous],
        yes_no[fins],
        legs,
        yes_no[tail],
        yes_no[domestic],
        yes_no[catsize]
    ]])

    prediction = model.predict(data)

    st.success(f"Predicted Animal Class: {class_names[prediction[0]]}")