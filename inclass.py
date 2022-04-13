import streamlit as st
import pandas as pd
import numpy as np


# Reference: https://github.com/streamlit/example-app-commenting/blob/main/streamlit_app.py
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

st.title('Deployment In-Class Example - CS5394')
space(2)
st.title('Button Clicking: ')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Click Me!', on_click=increment_counter)

st.write('Count = ', st.session_state.count)

space(3)
st.title('Loading & Displaying Data')

data = pd.read_csv("./hour.csv")
st.write(data)

space(1)

hist_values = np.histogram(
    data['windspeed'], bins=24)[0]

st.bar_chart(hist_values)

space(3)


# Reference: https://github.com/streamlit/example-app-commenting
st.title("Comment Section 💬")


