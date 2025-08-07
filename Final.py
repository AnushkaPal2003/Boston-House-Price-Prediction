import streamlit as st
import pandas as pd
from joblib import load

# Load scaler
scaler = load('scaler.joblib')

# Model options
model_names = {
    'Linear Regression': 'model_LR.joblib',
    'Ridge': 'model_Ridge.joblib',
    'Lasso': 'model_Lasso.joblib',
    'ElasticNet': 'model_ElasticNet.joblib',
    'Decision Tree': 'model_DecisionTree.joblib',
    'Random Forest': 'model_RandomForest.joblib',
    'XGBoost': 'model_XGBoost.joblib',
    'K-Nearest Neighbors': 'model_KNeighbors.joblib',
    'Support Vector Regressor': 'model_SVR.joblib',
    'Voting Regressor (Ensemble)': 'model_VotingRegressor.joblib'
}

# Title
st.title("🏠 Boston House Price Predictor")

# Model selection
selected_model_name = st.selectbox("Choose a model", list(model_names.keys()))
selected_model = load(model_names[selected_model_name])

# Input fields
zn = st.number_input("ZN", value=12.5)
indus = st.number_input("INDUS", value=7.5)
chas = st.selectbox("CHAS", [0, 1])
nox = st.number_input("NOX", value=0.45)
rm = st.number_input("RM", value=6.2)
age = st.number_input("AGE", value=65.0)
dis = st.number_input("DIS", value=4.2)
rad = st.number_input("RAD", value=4)
tax = st.number_input("TAX", value=300.0)
ptratio = st.number_input("PTRATIO", value=18.0)
b = st.number_input("B", value=390.0)
lstat = st.number_input("LSTAT", value=14.5)

# Create input DataFrame
input_data = pd.DataFrame({
    'zn': [zn],
    'indus': [indus],
    'chas': [chas],
    'nox': [nox],
    'rm': [rm],
    'age': [age],
    'dis': [dis],
    'rad': [rad],
    'tax': [tax],
    'ptratio': [ptratio],
    'b': [b],
    'lstat': [lstat]
})

# Predict
if st.button("Predict Price"):
    input_scaled = scaler.transform(input_data)
    prediction = selected_model.predict(input_scaled)
    st.success(f"🏡 Estimated Price using {selected_model_name}: ${prediction[0]:,.2f}")