import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=1)

out = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.write("You selected: ", out.capitalize())

greet(out)

from pyresis import read_ship, ship

file_name = out + ".shp"

out = read_ship.open(file_name)
ship = ship.Ship(**out.values())

st.write
