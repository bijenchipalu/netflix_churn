import pandas as pd
import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open("churn_model.pkl","rb"))

st.title("Netflix Churn Prediction")
st.write("Enter User information to predict churn probability")

age = st.slider("Age",18,70,25)
country = st.selectbox(
"Country",
["USA","India","UK","Cananda","Germany"]

)
subscription = st.selectbox(
"Subscription Type",
["Basic", "Standard", "Premium"]
)

watch_time = st.number_input(
"Watch Time",
0,1000,100
)

tenure = st.slider(
"Acount Tenure",
1,60,12
)

genre = st.selectbox(
"Favorite Genre",
["Action","Comedy","Drama","Sci-Fi","Romance"]
)

# convert impot to data frame

input_dict ={
'Age':[age],
'Watch_Time_hours':[watch_time],
'Tenure':[tenure],
'Country':[country],
'Subscription_type':[subscription],
'Favorite_Genre':[genre]
}

input_df = pd.DataFrame(input_dict)

input_df =pd.get_dummies(input_df)

# prediction

if st.button("Predict Churn"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("User likely to churn")
    else:
        st.success(" User will stay subscribed")