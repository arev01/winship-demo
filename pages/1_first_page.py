import streamlit as st
from mycomponent import mycomponent
from functions import menu, prompt

menu(counter=1)

my_output_value = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.write("You selected: " + my_output_value.capitalize())

with st.expander("Description"):
    prompt(my_output_value)

from pyresis import read_ship, ship

file_name = my_output_value + ".shp"

out = read_ship.open(file_name)
ship = ship.Ship(**out)

if 'ship' not in st.session_state:
    st.session_state['ship'] = ship

control = st.segmented_control("Specify ship size:",
                     ["Capacity", "Dimension"],
                    default="Capacity",
                    help="Currently unavailable",
                    )

if control == "Capacity":
    st.number_input("Gross tonnage (tons):", value=ship.gross_tonnage, disabled=True)
elif control == "Dimension":
    st.number_input("Length (m):", value=ship.length, disabled=True)
    st.number_input("Beam (m):", value=ship.beam, disabled=True)
    st.number_input("Draft (m):", value=ship.draft, disabled=True)
    st.number_input("Speed (kt):", value=ship.speed, disabled=True)
