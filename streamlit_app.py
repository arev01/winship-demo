import streamlit as st
from contextlib import contextmanager
from mycomponent import mycomponent

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

# ---- MAIN FUNCTION ----
def main():
    #---- ONGOING PROJECTS ----
    st.write("# Welcome to winship! 👋")
    out = mycomponent(my_input_value=50)
    
    # Display the output in Streamlit
    st.write("You selected: ", out.capitalize())

    st.divider()

    option = st.selectbox(
        "Wind assisted device:",
        ("Wing", "Rotor", "Sail", "Kite"),
    )

    st.divider()

    from nodes import nodes

    #Define origin and destination ports
    tab1, tab2 = st.tabs(["Origin", "Destination"])

    with tab1:
        origin = st.selectbox(
            "Select port of origin:",
            nodes.keys()
        )
    with tab2:
        destination = st.selectbox(
            "Select port of destination:",
            nodes.keys()
        )

    # Use a maritime network geograph
    from scgraph.geographs.marnet import marnet_geograph

    # Get the shortest path between 
    output = marnet_geograph.get_shortest_path(
        tup = ("latitude", "longitude"), 
        origin_node = {tup[i]: nodes[origin][i] for i, _ in enumerate(tup)}, 
        destination_node = {tup[i]: nodes[destination][i] for i, _ in enumerate(tup)}
    )
    st.write("Distance: ",output['length'])

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        output['coordinate_path'],
        columns = list(tup)
    )
    st.map(df, height=300)

    st.divider()

    buttons = [
        "Spring",
        "Summer",
        "Autumn",
        "Winter",
        "All year",
    ]

    with st_horizontal():
        for i, option in enumerate(buttons):
            st.button(option, key=f"button_{i}")

if __name__=='__main__':
    main()
