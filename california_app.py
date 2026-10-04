import numpy as np
import joblib
import streamlit as st

object=joblib.load('california.joblib')
model=object['model']
cols=object['columns']
#---------------------------------

st.title('California App')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} value : ')
    In.append(v)
if st.button('click'):
    out=model.predict([In])
    st.success(f"The Median House value is : {out}")
