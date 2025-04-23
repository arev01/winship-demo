import streamlit as st
from utils.functions import menu, prompt

menu(counter=4)

st.markdown("### FAQ/Guide")

st.markdown(
    """
    to navigate the different menus and press :material/bolt: to evaluate your favorite design.
    """
)

with st.expander("Step-by-step:"):
    st.markdown(
        """
        1. Click :material/sailing: and swipe left/right to choose your favorite ship.
        
        2. Click :material/air: and select your favorite wind device.

        3. Click :material/route: and select a port of origin and destination.

        4. Click XXX to 

        5. Click XXX to show this 
        
        """
    )

with st.expander("Methodology:"):
    st.markdown(
        """
        The tool works by balancing the aerodynamic and hydrodynamic forces of the ship. It takes into account the most important eﬀects of the wind powered devices to estimate the fuel and emission savings for a defined route (origin and destination port), ship design and speed as per [1].

        Due to the complexity of the problem, some approximations are made using basic ship theory:

        - For simplicity, the tool only solves one equation (movement along the longitudinal axis), assuming that the ship will naturally be balanced for all other motions.

        - Calm water resistance and hull/propeller interaction coefficients are given by Harvald [2] semi empirical method.

        - Propulsion efficiency is estimated using naval architecture’s rules of thumbs.

        - Added resistance due to wind and waves is accounted for by applying a sea margin of 20% regardless of the ship route.

        - Wind powered device operation typically can be calculated through lift and drag coefficients found in literature.

        - Wind data is derived from the ERA-5 dataset [3] (annually averaged).

        - WINSHIP uses generic ship models and wind devices with typical dimensions used in the maritime industry.

        - No interaction
        """
    )
    st.empty()
    st.markdown(
        """
        [1] European Maritime Safety Agency (2023), Potential of Wind-Assisted Propulsion for Shipping, EMSA, Lisbon.
        [2] Harvald S. A. (1983), Resistance and Propulsion of Ships, Wiley 1983, ISBN 0-89464-754-7.
        [3] Copernicus Climate Change Service (2017), ERA-5: Fifth generation of ECMWF atmospheric reanalyses of the global climate, Accessed March 2025.
        """
    )

#previous_page = st.button("Go back")
#if previous_page:
#        page_file = "./streamlit_app.py"
#        st.switch_page(page_file)
        
