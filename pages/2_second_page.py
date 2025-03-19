import streamlit as st
from mycomponent import mycomponent
from functions import greet
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
with st_horizontal():
    if st.button("<"):
        page_file = "./pages/1_first_page.py"
        # Switch to the selected page
        st.switch_page(page_file)
    if st.button("\>"):
        page_file = "./pages/3_third_page.py"
        # Switch to the selected page
        st.switch_page(page_file)

option = st.segmented_control("Wind assisted device:,"
    ["Wing", "Rotor", "Sail", "Kite"],
)

with st.container(height=393, border=True):
    cols_mr = st.columns([10.9, 0.2, 10.9])
    with cols_mr[0].container(height=350, border=False):
        st.image("./img/" + option.lower() + ".jpg")
    with cols_mr[1]:
        st.html(
            '''
                <div class="divider-vertical-line"></div>
                <style>
                    .divider-vertical-line {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        height: 320px;
                        margin: auto;
                    }
                </style>
            '''
        )
    with cols_mr[2].container(height=350, border=False):
        greet(option.lower())
