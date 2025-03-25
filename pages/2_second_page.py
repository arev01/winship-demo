import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=2)

option = st.selectbox("Wind assisted device:",
    ["Rotor", "Suction", "Wing", "Sail", "Kite"],
)

# HTML to add an image to a button
button_html = """
<a href='https://www.example.com' target='_blank'>
  <img src='./img/kite.jpg' alt='Button Image' style='width:100px;height:50px;'>
</a>
"""

# Display the button with an image
st.markdown(button_html, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("./img/" + option.lower() + ".jpg", width=40)
with col2:
    greet(option.lower())
