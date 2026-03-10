import streamlit as st
import numpy as np
import pandas as pd
import pickle

# LOAD MODEL
rfr = pickle.load(open('rfr.pickle','rb'))
X_train = pd.read_csv('X_train.csv')


#WEB APP
# Gender	Age	Height	Weight	Duration	Heart_Rate	Body_Temp

st.title("CALORIES BURNT PREDICTION")
# Gender = st.selectbox('Gender', X_train['Gender'])
# Age = st.selectbox('Age', X_train['Age'])
# Height = st.selectbox('Height', X_train['Height'])
# Weight = st.selectbox('Weight', X_train['Weight'])
# Duration = st.selectbox('Duration', X_train['Duration'])
# Heart_Rate = st.selectbox('Heart_Rate', X_train['Heart_Rate'])
# Body_Temp = st.selectbox('Body_Temp', X_train['Body_Temp'])

Gender = st.number_input("Enter the Gender: 0 for female and 1 for male",0,1)
Age = st.number_input("Enter your Age:",1,130)
Height = st.number_input("Enter your Height(in cms)")
Weight = st.number_input("Enter your Weight(in kgs)")
Duration = st.number_input("Enter the duration of your workout(in minutes)")
Heart_Rate = st.number_input("Enter your Heart_Rate(in bpm)")
Body_Temp = st.number_input("Enter your Body_Temp(in °C)")

#PREDICTION FUNCTION
def pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
    prediction = rfr.predict(features) 
    return prediction


result = pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)

if st.button('Predict'):
    if result:
        st.write(f"You had burnt {result} calories")   
