import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        visibility: hidden;
    }
</style>
""",
    unsafe_allow_html=True,
)

@st.dialog("❓ Help")
def help():
    st.markdown(
        """
        Use the buttons :material/arrow_back_ios::material/arrow_forward_ios:
        to navigate the different menus and choose your favorite design.
        
        Press :material/bolt: to run a prediction.
        """
    )
    
    tmp_checkbox = st.checkbox("I understand")

    
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
        if tmp_checkbox:
            # Switch to the selected page
            page_file = "./pages/1_first_page.py"
            st.switch_page(page_file)
        else:
            st.stop()
    previous_page = st.button("Methodology")
    if previous_page:
        page_file = "./pages/4_fourth_page.py"
        st.switch_page(page_file)

if __name__=='__main__':
    main()
