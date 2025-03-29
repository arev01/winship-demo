import streamlit as st

st.title("📚 Background")

st.markdown(
        """
        The tool works by balancing the aerodynamic and hydrodynamic forces of the ship. It takes into account the most important eﬀects of the wind powered devices to predict the ship speeds at various wind conditions.

        By determining the elapsed time around the course, a direct measure of the fuel and emission savings can be assessed.

        """
        )

        previous_page = st.button("Go back")
        if previous_page:
                page_file = "./streamlit_app.py"
                st.switch_page(page_file)
        
