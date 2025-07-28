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
    st.title("👋 Ahoy and welcome aboard!")
    app_path = 'http://localhost:8501'
    page_file_path = 'pages/page_4.py'
    page = page_file_path.split('/')[1][0:-3]  # get "page_4"
    st.write(
        """
        Ready to explore how auxiliary wind propulsion can clean up the shipping industry?
        """
    )
    
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
        next_page = st.button("Set sail")
        if next_page:
            # Switch to the selected page
            page_file = "./pages/page_1.py"
            st.switch_page(page_file)

    st.markdown(
        f'''
        For more information, check the <a href="{app_path}/{page}" target="_self">Resource</a> section.
        ''',
        
        unsafe_allow_html=True
    )
    
    st.badge("Disclaimer: This tool is intended for educational purpose only.")

if __name__=='__main__':
    main()
