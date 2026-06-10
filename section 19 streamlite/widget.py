import streamlit as st
import pandas as pd
# text input 
name=st.text_input("Enter your name")
if name:
    st.write(f"your name is :{name}")
    
#age with slider 

age=st.slider(f'your age is ',0,100,23)
if age:
    st.write(f"your age is : {age}") 
    
# option 
option=['python','c','java','c++']    
choice=st.selectbox('chose your option',option)
st.write(f'your favrite language is {choice}')

# upload a csv file 
upload_file=st.file_uploader('chose csv file ',type='csv')

if upload_file is not None:
    pd.read_csv(upload_file)
    st.write(pd)