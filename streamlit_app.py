import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
    
# ---- MAIN FUNCTION ----
def main():
    st.title("Welcome to winship! 👋")
    st.write(
        """
        A tool that estimates the performance of a ship equipped with wind powered devices in 3 simple steps: select ship type & size, choose device configuration and select a course.

        Accurate results plus a graphical output will be available in just a few seconds.

        The code works by balancing the aerodynamic and hydrodynamic forces of the ship. It takes into account the most important eﬀects of the wind powered devices to predict the ship speeds at various wind conditions.

        By determining the elapsed time around the course, a direct measure of the fuel and emission savings can be assessed.
        """
    )
    # Button to switch page
    next_page = st.button("Start")
    if next_page:
        # Switch to the selected page
        page_file = "./pages/1_first_page.py"
        st.switch_page(page_file)

if __name__=='__main__':
    main()
