import streamlit as st
import joblib
import numpy as np

model = joblib.load("zoo_random_forest.pkl")

yes_no = {
    "Yes": 1,
    "No": 0
}

class_names = {
    1: "🐘 Mammal",
    2: "🐦 Bird",
    3: "🐍 Reptile",
    4: "🐟 Fish",
    5: "🐸 Amphibian",
    6: "🐞 Bug",
    7: "🦑 Invertebrate"
}

descriptions = {
    "🐘 Mammal": "Warm-blooded animals that produce milk and usually have hair.",
    "🐦 Bird": "Animals with feathers, wings and most lay eggs.",
    "🐍 Reptile": "Cold-blooded vertebrates with scales.",
    "🐟 Fish": "Aquatic animals with fins and gills.",
    "🐸 Amphibian": "Animals that live both on land and in water.",
    "🐞 Bug": "Small six-legged invertebrates such as insects.",
    "🦑 Invertebrate": "Animals without a backbone."
}

if "page" not in st.session_state:
    st.session_state.page = "home"

if "prediction" not in st.session_state:
    st.session_state.prediction = ""

if st.session_state.page == "home":

    st.title("🦁 Zoo Animal Prediction")
    st.write("Select the animal characteristics below.")

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

        prediction = model.predict(data)[0]

        st.session_state.prediction = class_names[prediction]
        st.session_state.page = "result"

        st.rerun()


if st.session_state.page == "result":

    st.title("🎯 Prediction Result")

    st.success(f"Predicted Animal Class: {st.session_state.prediction}")

    st.info(descriptions[st.session_state.prediction])

    if st.button("🔙 Predict Another Animal"):
        st.session_state.page = "home"
        st.rerun()