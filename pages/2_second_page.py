import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=2)

option = st.selectbox("Wind assisted device:",
    ["Rotor", "Suction", "Wing", "Sail", "Kite"],
)

# HTML to add an image to a button
from streamlit_image_select import image_select
img = image_select("Label", ["./img/rotor.jpg", "./img/suction.jpg", "./img/wing.jpg"])
st.write(img)

col1, col2 = st.columns(2)
with col1:
    st.image("./img/" + option.lower() + ".jpg", width=40)
with col2:
    greet(option.lower())
