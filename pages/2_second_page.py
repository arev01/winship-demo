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

import numpy as np

# Get lift and drag coefficients
lift_coef, drag_coef = np.loadtxt(img[6:-4] + ".dat"), comments="#", delimiter="\t", usecols=(1, 2), unpack=False)

# Choose units, size 
if img[6:-4] == "kite":
    sizes_list = [
        "300", "500", "1000"
    ]
else:
    sizes_list = [
        "18x3", "24x4", "30x5"
    ]

if ship.gross_tonnage < 10000:
    units, size = 1, sizes_list[0]
elif ship.gross_tonnage >= 10000 and ship.gross_tonnage < 50000:
    units, size = 2, sizes_list[1]
elif ship.gross_tonnage >= 50000 and ship.gross_tonnage < 100000:
    units, size = 4, sizes_list[1]
else:
    units, size = 4, sizes_list[2]

choice = st.segmented_control(["Quantity", "Dimension"], help=…)

if choice == "Quantity":
    st.number_input("Units (-):", [1, 2, 4], default=units, disabled=True)
else:
    st.dropdown_select("Size (m2):", sizes_list, default=size, disabled=True)
