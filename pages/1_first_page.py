import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=1)

my_output_value = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.write("You selected: ", my_output_value.capitalize())

st.write("<a href='#' id='my-link'>Click me</a>", unsafe_allow_html=True)

if st.button("Click me", type="primary"):
    st.write("Clicked")

st.button("Another button!")

st.markdown(
    """
    <style>
    button[kind="primary"] {
        background: none!important;
        border: none;
        padding: 0!important;
        color: black !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
    }
    button[kind="primary"]:hover {
        text-decoration: none;
        color: black !important;
    }
    button[kind="primary"]:focus {
        outline: none !important;
        box-shadow: none !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

greet(my_output_value)

from pyresis import read_ship, ship

file_name = my_output_value + ".shp"

out = read_ship.open(file_name)
ship = ship.Ship(**out.values())

length = st.number_input("meters length", value=ship.length)
beam = st.number_input("meters beam", value=ship.beam)
draft = st.number_input("meters draft", value=ship.draft)
speed = st.number_input("knots speed", value=ship.speed)

import numpy as np

data = np.array(
    [
        (speed, ship.resistance(speed) / 1000.0)
        for speed in np.arange(0.1, 35.0, 0.5)
    ],
)

st.write(data)
