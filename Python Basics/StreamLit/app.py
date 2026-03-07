import streamlit as st
import pandas as pd
import numpy as np

## Title of app
st.title("My first app")

## create a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4], 
    'second column': [10, 20, 30, 40]
})

## display the dataframe
st.write("Here's our first attempt at using data to create a table:", df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
)
st.line_chart(chart_data)