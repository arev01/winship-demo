import streamlit as st
from contextlib import contextmanager

HORIZONTAL_STYLE = """
<style class="hide-element">
    /* Hides the style container and removes the extra spacing */
    .element-container:has(.hide-element) {
        display: none;
    }
    /*
        The selector for >.element-container is necessary to avoid selecting the whole
        body of the streamlit app, which is also a stVerticalBlock.
    */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) {
        display: flex;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: baseline;
        justify-content: flex-end;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        border-color: red;
    }
    */
</style>
"""

@contextmanager
def st_horizontal():
    st.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.container():
        st.markdown('<span class="hide-element horizontal-marker"></span>', unsafe_allow_html=True)
        yield

# Button to switch page
def menu():
    counter = 0
    page_lst = [
        "./pages/1_first_page.py",
        "./pages/2_second_page.py",
        "./pages/3_third_page.py"
    ]
    with st_horizontal():
        if st.button(":material/home:"):
            counter = 0
            page_file = "./streamlit_app.py"
            # Switch to the selected page
            st.switch_page(page_file)
        if st.button("<"):
            counter -= 1
            page_file = page_lst[counter]
            # Switch to the selected page
            st.switch_page(page_file)
        if st.button("\>"):
            counter += 1
            page_file = page_lst[counter]
            # Switch to the selected page
            st.switch_page(page_file)
