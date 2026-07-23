import streamlit as st
import pickle
st.write("Hello,let's register first")
Pregnancies=st.number_input("Enter the no.of Pregnancies(in number)")
Glucose=st.number_input("Enter the gulcose(in number)")
BloodPressure=st.number_input("Enter the bloodpressure(in number)")
SkinThickness=st.number_input("Enter the skinthickness(in number)")
BMI=st.number_input("Enter the bmi(in number)")
Insulin=st.number_input("Enter the insulin count")
DiabetesPedigreeFunction=st.number_input("Enter the diabetes(in number)")
Age=st.number_input("Enter the age(in number)")
with open(r"C:\Users\vanmika AG\OneDrive\Desktop\Akira 2\diabetes.pkl", 'rb') as file:
    model = pickle.load(file)
if st.button('diabetes'):
   st.write(model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]))