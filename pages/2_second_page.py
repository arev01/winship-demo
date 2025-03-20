import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=2)

option = st.segmented_control("Wind assisted device:",
    ["Rotor", "Suction", "Wing", "Sail", "Kite"],
)

col1, col2 = st.columns(2)
with col1:
    st.image("./img/" + option.lower() + ".jpg", width=200)
with col2:
    greet(option.lower())
