import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=1)

my_output_value = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.write("You selected: ", my_output_value.capitalize())

greet(my_output_value)

from pyresis import read_ship, ship

file_name = my_output_value + ".shp"

out = read_ship.open(file_name)
ship = ship.Ship(**out.values())

length = st.number_input("meters length", value=ship.length)
beam = st.number_input("meters beam", value=ship.beam)
draft = st.number_input("meters draft", value=ship.draft)
speed = st.number_input("knots speed", value=ship.speed)

