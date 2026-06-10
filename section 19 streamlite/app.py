import streamlit as st
import pandas as pd
import numpy as np 

st.title("this is my app title")
st.write("my first streamlit app")

# create a simple data frame
df=pd.DataFrame({
    'first colm':[2,3,4,5],
    '2nd column':[10,20,30,40]
}
)
# disply the dataframe
st.write(df)

# crate a line chart
chart=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.bar_chart(chart)