import streamlit as st
import pickle 
pickle_in=open('SalaryPp.pkl','rb')
model=pickle.load(pickle_in)

years=st.number_input('years of experience')
if st.button('Predict'):
  salary=model.predict([[years]])
  st.success(f'Salary predicted is {salary}')
