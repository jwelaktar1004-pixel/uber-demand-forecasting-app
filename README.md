# 🚖 Uber Trip Demand Forecasting Dashboard

A production-ready Machine Learning web application that predicts daily Uber trip demand using historical operational data and engineered time-series features.

🔗 **Live App:** https://uber-demand-forecasting-app-nxqtqg88rs5il3dqsxshjb.streamlit.app/ 
📂 **GitHub Repository:** https://github.com/jwelaktar1004-pixel/uber-demand-forecasting-app  

---

## 📌 Project Overview

This project builds an end-to-end Machine Learning pipeline to forecast daily trip demand for Uber dispatch bases.

The goal is to help optimize:
- 🚗 Fleet allocation
- 📈 Demand planning
- 🏢 Dispatch efficiency
- 📊 Operational strategy

The model captures seasonality, lag trends, and base-level variations to provide realistic demand forecasts.

---

## 🧠 Machine Learning Approach

### ✅ Model Used:
Random Forest Regressor

### ✅ Validation Strategy:
Time-based train-test split (to preserve temporal order)

### ✅ Feature Engineering:
- Active Vehicles
- Day of Week
- Month
- Weekend Indicator
- Previous Day Demand (Lag-1)
- Previous Week Demand (Lag-7)
- Trips Per Vehicle
- Dispatch Base (One-Hot Encoded)

### ✅ Total Features:
12 engineered features

---

## 📊 Business Impact

This solution can help ride-sharing operations:

- Optimize driver deployment
- Reduce idle fleet time
- Improve high-demand preparedness
- Support data-driven operational decisions
- Increase dispatch efficiency

The forecasting model enables proactive planning instead of reactive management.

---

## 🖥️ Web Application

The model is deployed using **Streamlit** as an interactive dashboard.

### Features:
- Clean professional UI
- Real-time prediction
- One-click demand forecasting
- Interactive visualization using Plotly
- Fully cloud deployed

---

## ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Streamlit
- Git & GitHub

---

## 🚀 Deployment

The application is deployed on **Streamlit Cloud**.

To run locally:

```bash
pip install -r requirements.txt
streamlit run app.py

👨‍💻 Author

Jwel Aktar
Data Science Enthusiast | Machine Learning Developer | Data Science Mentor

If you found this project useful, feel free to ⭐ the repository.
