import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=1)

my_output_value = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.markdown("You selected: " + my_output_value.capitalize(), 
         help="""A multi-purpose ship designed to transport 
         a wide variety of goods and commodities.""")

from pyresis import read_ship, ship

file_name = my_output_value + ".shp"

out = read_ship.open(file_name)
ship = ship.Ship(**out)

control = st.segmented_control("Specify ship size:",
                     ["Capacity", "Dimension"],
                    default="Capacity",
                    )

if control == "Capacity":
    st.number_input("tons deadweight", value=ship.deadweight, disabled=True)
elif control == "Dimension":
    st.number_input("meters length", value=ship.length, disabled=True)
    st.number_input("meters beam", value=ship.beam, disabled=True)
    st.number_input("meters draft", value=ship.draft, disabled=True)
    st.number_input("knots speed", value=ship.speed, disabled=True)
