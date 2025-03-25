import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=2)

from streamlit_image_select import image_select
img = image_select("Label", [
    "./img/rotor.jpg", 
    "./img/suction.jpg", 
    "./img/wing.jpg", 
    "./img/sail.jpg", 
    "./img/kite.jpg", 
])
st.write(dir(img))
st.write(type(img))
st.markdown("You selected: " + img[6:-4].capitalize(), 
            help="""
            A gigantic rig deployed above the ship to assist 
            in pulling the ship through the water."""
           )
