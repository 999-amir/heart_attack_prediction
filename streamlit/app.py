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
age = st.number_input('age', 20, 100)
gender = st.selectbox('Male', 'Female')
height = st.select_slider('height', [80, 200])
weight = st.select_slider('weight', [50, 120])
blood_pressure = st.text_input('blood pressure', '120/80')
cholesterol = st.number_input('cholestrol', 50, 400)
glucose = st.number_input('glucose', 30, 200)
smoker = st.select_box('smoke', 'Yes', 'No')
exercise = st.number_input('exercise', 0, 500)
