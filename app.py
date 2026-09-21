import streamlit as st
import os
from diet import bmi_calculator,bmr_calculator,tdee_calculator,calories_target

st.title("AI Health Assistant 😀")
st.write("Personal Health Assistant and Diet Recomandation Agent")
st.header("Health information")
st.sidebar.header("👻Your Information")

gender=st.sidebar.selectbox("Gender",["Male","Female"])
age=st.sidebar.number_input("Age",1,100)
weight=st.sidebar.number_input("Weight(KG)",1,120)
height=st.sidebar.number_input("Height(CM)",100,200)
activity=st.sidebar.selectbox("Activity",[
        "Sendentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active",
        "Extra Active"])
aim=st.sidebar.selectbox("AIM",["weight maintain","weight loss","weight gain"]) 
##----------------------##       
bmi=bmi_calculator(weight,height)
bmr=bmr_calculator(gender,age,weight,height)
tdee=tdee_calculator(bmr,activity)
calorie=calories_target(tdee,aim)
##------------------#
col1,col2,col3,col4=st.columns(4)
col1.metric("BMI",bmi)
col2.metric("BMR",f"{bmr} Kcal")
col3.metric("TDEE",f"{tdee} Kcal")
col4.metric("Calorie target",f"{calorie} Kcal")