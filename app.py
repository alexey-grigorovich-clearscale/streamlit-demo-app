# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# First, let's display page title and a welcome message
# Title
st.title('Streamlit Demo App')

# Regular paragaph text
st.write("This is a simple demo of Streamlit's capabilities.")

# Streamlit also supports top navs, sidebars, and more layout and typography options.

# Second, let's generate a mock dataset of squares of numbers between 1 and 10, and
# display it as a table as well as a line chart.
#
# In practice, the data may come from a database, a CSV file on S3, or a call to an external API.
#
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
