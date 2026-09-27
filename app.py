import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Food Delivery Time Prediction",
    page_icon="🍔",
    layout="centered")

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load("model_8_features.pkl")
feature_columns = joblib.load("feature_columns_8.pkl")

# -----------------------------
# TITLE
# -----------------------------

st.markdown(
    "<h1 style='text-align: center;'>🍔 FOOD DELIVERY TIME PREDICTION</h1>",
    unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center;'>Predict estimated food delivery time using delivery and traffic details.</p>",
    unsafe_allow_html=True)

st.divider()

# -----------------------------
# DELIVERY DETAILS
# -----------------------------

st.subheader("👤 DELIVERY DETAILS")
col1, col2 = st.columns(2)
with col1:
    delivery_age = st.number_input(
        "Delivery Person Age",
        min_value=18,
        max_value=60,
        value=25)
    delivery_rating = st.number_input(
        "Delivery Person Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.5,
        step=0.1)
    multiple_deliveries = st.number_input(
        "Multiple Deliveries",
        min_value=0,
        max_value=5,
        value=1)
with col2:
    delivery_distance = st.number_input(
        "Delivery Distance (km)",
        min_value=0.0,
        value=5.0,
        step=0.1)
    vehicle_condition = st.number_input(
        "Vehicle Condition",
        min_value=0,
        max_value=3,
        value=2)
    pickup_delay = st.number_input(
        "Pickup Delay (minutes)",
        min_value=0.0,
        value=10.0,
        step=0.1)

st.divider()

# -----------------------------
# TRAFFIC & WEATHER
# -----------------------------

st.subheader("🌦️ TRAFFIC & WEATHER")
col1, col2 = st.columns(2)
with col1:
    traffic = st.selectbox(
        "Road Traffic Density",
        ["High", "Jam", "Low", "Medium"])
with col2:
    weather = st.selectbox(
        "Weather",
        ["Cloudy", "Fog", "Sandstorms", "Stormy", "Sunny", "Windy"])

st.divider()

# -----------------------------
# INPUT DATA
# -----------------------------

input_data = {
    "Delivery_person_Ratings": delivery_rating,
    "multiple_deliveries": multiple_deliveries,
    "Delivery_Distance": delivery_distance,
    "Delivery_person_Age": delivery_age,
    "Vehicle_condition": vehicle_condition,
    "Pickup_Delay": pickup_delay}

# Traffic encoding

input_data["Road_traffic_density_Jam"] = (1 if traffic == "Jam" else 0)

input_data["Road_traffic_density_Low"] = (1 if traffic == "Low" else 0)

input_data["Road_traffic_density_Medium"] = (1 if traffic == "Medium" else 0)

# Weather encoding

input_data["Weatherconditions_conditions Fog"] = (1 if weather == "Fog" else 0)

input_data["Weatherconditions_conditions Sandstorms"] = (1 if weather == "Sandstorms" else 0)

input_data["Weatherconditions_conditions Stormy"] = (1 if weather == "Stormy" else 0)

input_data["Weatherconditions_conditions Sunny"] = (1 if weather == "Sunny" else 0)

input_data["Weatherconditions_conditions Windy"] = (1 if weather == "Windy" else 0)

# Convert to DataFrame

input_df = pd.DataFrame([input_data])
input_df = input_df[feature_columns]

# -----------------------------
# PREDICTION
# -----------------------------

st.subheader("🚀 GET PREDICTION")
if st.button(
    "PREDICT DELIVERY TIME",
    use_container_width=True):

    prediction = model.predict(input_df)
    predicted_time = round(prediction[0], 2)

    # Prediction result

    st.divider()
    st.subheader("⏱️ ESTIMATED DELIVERY TIME")
    st.metric(
        label="PREDICTED TIME",
        value=f"{predicted_time} MINUTES")

    # Delivery insight

    st.subheader("💡 DELIVERY INSIGHT")
    if predicted_time <= 20:
        st.success("The predicted delivery time is relatively short.")
    elif predicted_time <= 35:
        st.info("The predicted delivery time is moderate.")
    else:
        st.warning("The predicted delivery time is relatively long.")

    # Input summary

    st.subheader("📋 DELIVERY DETAILS")
    result_data = {
        "Delivery Person Age": delivery_age,
        "Delivery Person Rating": delivery_rating,
        "Multiple Deliveries": multiple_deliveries,
        "Delivery Distance": f"{delivery_distance} km",
        "Vehicle Condition": vehicle_condition,
        "Pickup Delay": f"{pickup_delay} minutes",
        "Traffic": traffic,
        "Weather": weather}
    result_df = pd.DataFrame(
        result_data.items(),
        columns=["DETAIL", "VALUE"])
    st.table(result_df)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:
    st.title("📌 ABOUT THE PROJECT")
    st.write(
        "A machine learning application that "
        "predicts food delivery time based on "
        "delivery and environmental factors.")
    st.divider()
    st.subheader("🤖 MODEL")
    st.write("Random Forest Regressor")
    st.divider()
    st.subheader("📊 MODEL PERFORMANCE")
    st.write("MAE: 3.23 minutes")
    st.write("R² SCORE: 80.62%")
    st.divider()