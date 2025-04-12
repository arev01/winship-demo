import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    section[data-testid="stSidebar"][aria-expanded="true"]{
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)

    
# ---- MAIN FUNCTION ----
def main():
    st.title("👋 Welcome to winship!")
    st.write(
        """
        A tool that evaluates the potential of a WINd-assisted SHIP in 3 simple steps: select ship type & size, choose device configuration and select a course.

        Accurate results plus a graphical output will be available in just a few seconds.
        """
    )
    # Button to switch page
    next_page = st.button("Start now", on_click=help)
    if next_page:
        # Switch to the selected page
        page_file = "./pages/1_first_page.py"
        st.switch_page(page_file)
    previous_page = st.button("Methodology")
    if previous_page:
        page_file = "./pages/4_fourth_page.py"
        st.switch_page(page_file)

if __name__=='__main__':
    main()
