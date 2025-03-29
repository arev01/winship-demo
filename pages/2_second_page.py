import streamlit as st
from mycomponent import mycomponent
from functions import prompt
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
st.markdown("You selected: " + img[6:-4].capitalize())

with st.expander("Description"):
    prompt(img[6:-4])
