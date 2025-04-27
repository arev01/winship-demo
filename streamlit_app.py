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
        A tool that evaluates the potential of a WINd-assisted SHIP in 3 simple steps: choose ship type, choose wind device and create shortest route.

        Accurate results plus a graphical output will be available in just a few seconds.

        For more information, see:
        """
    )

    st.page_link("./pages/page_4.py", label="Information", icon="📚")
    
    # Button to switch page
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        next_page = st.button("En avant toute !")
        if next_page:
            # Switch to the selected page
            page_file = "./pages/page_1.py"
            st.switch_page(page_file)

    st.badge("Disclaimer: This tool is intended for educational purpose only.")

if __name__=='__main__':
    main()
