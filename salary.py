import streamlit as st
import pickle
import numpy as np
st.write("Hello,let's register first")
EducationLevel=st.text_input("Enter the Education Level")
JobTitle=st.text_input("Enter the Job Title")
YearsofExperience=st.text_input("Enter the Years of Experience")
with open(r'C:\Users\vanmika AG\OneDrive\Desktop\Akira 2\bala.pkl','rb') as file:
    model = pickle.load(file)
with open(r'C:\Users\vanmika AG\OneDrive\Desktop\Akira 2\label.pkl','rb') as file:
    salary1 = pickle.load(file)
with open(r'C:\Users\vanmika AG\OneDrive\Desktop\Akira 2\label1.pkl','rb') as file:
    salary2 = pickle.load(file)
if st.button('salary'):
   EducationLevel=salary1.transform([EducationLevel])
   JobTitle=salary2.transform([JobTitle])
   data=[EducationLevel,JobTitle,np.array([YearsofExperience])]
   data=np.array(data).reshape(1,-1)
prediction = model.predict(data)
st.write("Predicted Salary:", prediction[0])
 #  st.write(model.predict([[data]]))