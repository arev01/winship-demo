import streamlit as st
from streamlit_javascript import st_javascript

url = st_javascript("await fetch('').then(r => window.parent.location.href)")[0:-5]
st.write(url)


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
    page_file = './pages/page_4.py'
    page = page_file.split('/')[-1][0:-3]  # get "page_4"
    st.write(
        """
        Ready to explore how auxiliary wind propulsion can clean up the shipping industry?
        """
    )
    
    # Button to switch page
    next_page = st.button("Set sail")
    if next_page:
        # Switch to the selected page
        page_file = "./pages/page_1.py"
        st.switch_page(page_file)

    st.markdown(
        f'''
        For more information, check out the <a href="{url}/{page}" target="_self">Resources</a> section.
        ''',
        
        unsafe_allow_html=True
    )
    
    st.badge("Disclaimer: Use this tool at your own risk.")

if __name__=='__main__':
    main()
