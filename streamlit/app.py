import pandas as pd
import joblib
from utils import PreProcessor
import streamlit as st
import numpy as np

st.title('hello there \n this is a webapp than can predict your heart attack with +99% precision score')
age = st.number_input('Age', 20, 100)
gender = st.selectbox('Gender', ['Male', 'Female'])
height = st.select_slider('Height(cm)', np.arange(80, 201))
weight = st.select_slider('Weight(kg)', np.arange(50, 121))
blood_pressure = st.text_input('Blood Pressure(mmHg)', '120/80')
cholesterol = st.number_input('Cholesterol(mg/dL)', 50, 400)
glucose = st.number_input('Glucose(mg/dL)', 30, 200)
smoke = st.selectbox('Smoker', ['Yes', 'No'])
exercise = st.number_input('Exercise(hours/week)', 0, 500)

model = joblib.load('HeartAttack.joblib')
def predict(data):
    data_features = ['ID', 'Name', 'Age', 'Gender', 'Height(cm)', 'Weight(kg)',
        'Blood Pressure(mmHg)', 'Cholesterol(mg/dL)', 'Glucose(mg/dL)',
        'Smoker', 'Exercise(hours/week)']
    data_df = pd.DataFrame([['n', 'n']+data], columns=data_features)
    return model.predict(data_df)[0]
data = [23, 'Male', 173, 56, '120/80', 170, 80, 'No', 2]
if predict(data)==0:
  st.baloons()
  st.success("you won't get hear attack")
else:
  st.warning('you may have heart attack')
