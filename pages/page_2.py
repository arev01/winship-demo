import streamlit as st
from utils.functions import menu, prompt
from lib.pyaero import wind, navigation

menu(counter=2)

st.markdown("### Select a device")

if 'ship' not in st.session_state:
    st.error("No ship selected")
else:

    from streamlit_image_select import image_select

    img = image_select("", [
        "./resources/img/rotor.jpg", 
        "./resources/img/suction.jpg", 
        "./resources/img/wing.jpg", 
        "./resources/img/sail.jpg", 
        "./resources/img/kite.jpg", 
    ])

    st.markdown("You selected: " + img.split("/")[3][:-4].capitalize())

    with st.expander("Description"):
        prompt(img.split("/")[3][:-4])

    import numpy as np

    # Create Wind() class object
    wind = wind.Wind()

    # Get lift and drag coefficients
    file_name = img.split("/")[3][:-4] + ".dat"
    path_to_file = "./resources/prf/" + file_name

    try:
        wind.lift_coef, wind.drag_coef = np.loadtxt(path_to_file, comments="#", usecols=(1, 2), unpack=True)

        # Choose units, size 
        if img[6:-4] == "kite":
            sizes_list = [
                "300", "500", "1000"
            ]
        else:
            sizes_list = [
                "18x3", "24x4", "30x5"
            ]

        if st.session_state['ship'].gross_tonnage < 10000:
            units, size = 1, 0
        elif st.session_state['ship'].gross_tonnage >= 10000 \
        and st.session_state['ship'].gross_tonnage < 50000:
            units, size = 2, 1
        elif st.session_state['ship'].gross_tonnage >= 50000 \
        and st.session_state['ship'].gross_tonnage < 100000:
            units, size = 4, 1
        else:
            units, size = 4, 2

        control = st.segmented_control("Specify device size:",
                            [],
                            help="Currently unavailable",
                            )

        st.number_input("Units (-):", value=units, disabled=True)
        st.selectbox("Size (m2):", sizes_list, index=size, disabled=True)

        # Correct attributes
        wind.units = units
        wind.size = np.prod([float(i) for i in sizes_list[size].split("x")])

        st.session_state['wind'] = wind

    except:
        st.error("Not available yet")