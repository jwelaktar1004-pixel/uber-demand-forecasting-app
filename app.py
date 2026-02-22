# ==============================
# UBER DEMAND FORECASTING APP
# Production Ready Version
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Uber Demand Forecasting",
    page_icon="🚖",
    layout="wide"
)

# ------------------------------
# Load Model
# ------------------------------
@st.cache_resource
def load_model():
    with open("uber_demand_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ------------------------------
# Header
# ------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B;'>
        🚖 Uber Trip Demand Forecasting Dashboard
    </h1>
    <p style='text-align: center; font-size:18px;'>
        Predict daily trip demand using Machine Learning
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("📊 Model Information")

st.sidebar.markdown("""
**Model Used:** Random Forest Regressor  
**Total Features:** 12  
**Validation Method:** Time-based Split  
**Use Case:** Daily Trip Demand Forecasting  
""")

st.sidebar.markdown("---")
st.sidebar.write("Built by Jwel Aktar 🚀")

# ------------------------------
# Inputs
# ------------------------------
st.subheader("📥 Enter Input Features")

col1, col2 = st.columns(2)

with col1:
    active_vehicles = st.number_input("Active Vehicles", min_value=0, value=5)
    day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 1)
    month = st.slider("Month", 1, 12, 7)
    is_weekend = st.selectbox("Is Weekend?", [0, 1])

with col2:
    prev_day = st.number_input("Previous Day Trips", min_value=0, value=7)
    prev_week = st.number_input("Previous Week Trips", min_value=0, value=8)
    trips_per_vehicle = st.number_input("Trips Per Vehicle", min_value=0.0, value=300.0)
    dispatch = st.selectbox(
        "Select Dispatch Base",
        ["B02598", "B02617", "B02682", "B02764", "B02765"]
    )

st.markdown("---")

# ------------------------------
# Prediction
# ------------------------------
if st.button("🚀 Predict Demand"):

    # One-hot encoding
    dispatch_b02598 = 1 if dispatch == "B02598" else 0
    dispatch_b02617 = 1 if dispatch == "B02617" else 0
    dispatch_b02682 = 1 if dispatch == "B02682" else 0
    dispatch_b02764 = 1 if dispatch == "B02764" else 0
    dispatch_b02765 = 1 if dispatch == "B02765" else 0

    lag_1 = prev_day
    lag_7 = prev_week

    # 🔥 IMPORTANT: Use DataFrame with exact feature names
    input_df = pd.DataFrame([{
        "active_vehicles": active_vehicles,
        "day_of_week": day_of_week,
        "trips_per_vehicle": trips_per_vehicle,
        "month": month,
        "is_weekend": is_weekend,
        "lag_1": lag_1,
        "lag_7": lag_7,
        "dispatching_base_number_B02598": dispatch_b02598,
        "dispatching_base_number_B02617": dispatch_b02617,
        "dispatching_base_number_B02682": dispatch_b02682,
        "dispatching_base_number_B02764": dispatch_b02764,
        "dispatching_base_number_B02765": dispatch_b02765
    }])

    prediction = model.predict(input_df)[0]

    # ------------------------------
    # Output
    # ------------------------------
    st.success("Prediction Generated Successfully!")

    st.metric(
        label="📈 Predicted Daily Trips",
        value=int(prediction)
    )

    # Chart
    result_df = pd.DataFrame({
        "Category": ["Predicted Trips"],
        "Trips": [prediction]
    })

    fig = px.bar(
        result_df,
        x="Category",
        y="Trips",
        color="Category",
        title="Predicted Trip Demand",
        text_auto=True
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ------------------------------
# Footer
# ------------------------------
st.markdown(
    "<center>© 2026 Uber Trip Demand Forecasting | Built with Streamlit 🚀</center>",
    unsafe_allow_html=True
)