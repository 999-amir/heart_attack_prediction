import pandas as pd
import joblib
from utils import PreProcessor
import streamlit as st

# model = joblib.load('HeartAttack.joblib')
# def predict(data):
#     data_features = ['ID', 'Name', 'Age', 'Gender', 'Height(cm)', 'Weight(kg)',
#         'Blood Pressure(mmHg)', 'Cholesterol(mg/dL)', 'Glucose(mg/dL)',
#         'Smoker', 'Exercise(hours/week)']
#     data_df = pd.DataFrame([['n', 'n']+data], columns=data_features)
#     return model.predict(data_df)[0]
# data = [23, 'Male', 173, 56, '120/80', 170, 80, 'No', 2]
# predict(data)

st.title('hello there \n this is a webapp than can predict your heart attack with +99% precision score')
