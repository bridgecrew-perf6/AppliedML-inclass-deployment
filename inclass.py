import streamlit as st
import pandas as pd
import numpy as np

# For comment section, referenced below
from datetime import datetime
from utils import db


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

st.write("**Comments:**")

for index, entry in enumerate(comments.itertuples()):
    st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

    is_last = index == len(comments) - 1
    is_new = "just_posted" in st.session_state and is_last
    if is_new:
        st.success("☝️ Your comment was successfully posted.")

space(2)

# Insert comment

st.write("**Add your own comment:**")
form = st.form("comment")
name = form.text_input("Name")
comment = form.text_area("Comment")
submit = form.form_submit_button("Add comment")

if submit:
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    db.insert(conn, [[name, comment, date]])
    if "just_posted" not in st.session_state:
        st.session_state["just_posted"] = True
    st.experimental_rerun()
