import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Streamlit Demo App')

# Text
st.write("This is a simple demo of Streamlit's capabilities.")

# Data
data = pd.DataFrame({
    'numbers': range(1, 11),
    'squares': [x ** 2 for x in range(1, 11)]
})

# Table
st.write("Here's a simple table of numbers and their squares:")
st.table(data)

# Chart
st.write("And a chart visualizing the same data:")
st.line_chart(data)

# Map
st.write("Streamlit also supports mapping. Here's a random scatter plot on a map:")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# Widgets
st.write("Streamlit includes interactive widgets. Try adjusting the slider:")
slider_val = st.slider('Select a range', 0, 100, 25)
st.write('You selected:', slider_val)
