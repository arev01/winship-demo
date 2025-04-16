import streamlit as st

st.title("📚 Methodology")

st.markdown(
        """
        The tool works by balancing the aerodynamic and hydrodynamic forces of the ship. It takes into account the most important eﬀects of the wind powered devices to predict the ship speeds at various wind conditions.

        A methodology to estimate the fuel and emission savings for a defined route (origin and destination port), ship design and speed is provided in [1].

        Due to the complexity of the problem, some approximations are made using basic ship theory:

        - For simplicity, the tool only solves one equation (movement along the longitudinal axis), assuming that the ship will naturally be balanced for all other motions.

        - Calm water resistance and hull/propeller interaction coefficients are given by Harvald [2] semi empirical method.

        - Propulsion efficiency is estimated using naval architecture’s rules of thumbs.

        - Added resistance due to wind and waves is accounted for by applying a sea margin of 10-25% based on the ship route.

        - Wind powered device operation typically can be calculated through lift and drag coefficients found in literature.

         - Wind data is derived from the ERA-5 [3] database (annual average).

        - Generic models. Typical dimensions.

        - No interaction

        [1] European Maritime Safety Agency (2023), Potential of Wind-Assisted Propulsion for Shipping, EMSA, Lisbon
        [2] Harvald S. A. (1983), Resistance and Propulsion of Ships, Wiley 1983, ISBN 0-89464-754-7
        [3] Copernicus
        """
)

previous_page = st.button("Go back")
if previous_page:
        page_file = "./streamlit_app.py"
        st.switch_page(page_file)
        
