import streamlit as st
import pandas as pd
import numpy as np
import os
import tarfile
import urllib

st.title('In-Class Example - CS5394')

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Click Me!', on_click=increment_counter)

st.write('Count = ', st.session_state.count)

DOWNLOAD_ROOT = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset/hour"

data = pd.read_csv("hour.csv")
st.write(data)

hist_values = np.histogram(
    data['windspeed'], bins=24)[0]

st.bar_chart(hist_values)
 
