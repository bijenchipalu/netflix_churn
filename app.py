import pandas as pd
import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open("churn_model.pkl","rb"))

st.title("Netflix Churn Prediction")

age = st.slider("Age",18,70)
tenuer = st.slider("Month Subscribed",1,60)

if st.button("Predict"):
    prediction = model.predict([[age,1,2,15.99,tenure,120,3,1,2]])

    if prediction[0] == 1:
        st.error("User likely to churn")
    else:
        st.success("User Likely to Stay")
