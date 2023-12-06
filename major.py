import streamlit as st
import datetime

import pandas as pd


import pickle

load_model = pickle.load(open('Linear.pkl', 'rb'))


st.title("         CAR PRICE PREDICTION APP")
st.write("THIS APP PREDICTS THE PRICE OF USED CARS IN lakhs")

st.write("")
st.write("")

p1= st.number_input('Present used car prices', 2.5, 30.5, step=0.5)
p2= st.number_input("The total kilometres covered by the car", 1000, 10000000, step=1000)
b1= st.selectbox("Select the fuel type of the car", ('Petrol' ,'Diesel' ,'CNG'))
if b1 == "Petrol":
    p3=0
elif b1 =="Diesel":
    p3=1
elif b1 == "CNG":
    p3=2

b2= st.selectbox("Select if you are an individual or a dealer",( 'Individual', 'Dealer'))


if b2 == "Dealer":
    p4=0
elif b2 == "Individual":
    p4=1

b3= st.selectbox("Select the transmission type", ('Automatic', 'Manual'))


if b3 == "Manual":
    p5=0
elif b3 == "Automatic":
    p5=1

p6 = st.slider("select the number of owners", 0,3)

date_time=datetime.datetime.now()

years= st.number_input('Select year that the car was bought', 1995, date_time.year)
p7 = date_time.year-years

data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'years number':p7
}, index=[0])

try:
    if st.button('Predict'):
        pred= load_model.predict(data_new)
        if pred>0:
            st.success('The car can be sold for {:.2}lakhs'.format(pred[0]))
        else:
            st.warning('the car can not be sold')
except:
    st.warning('An error occurred')


    