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
    st.write("Ship type:", out.capitalize())

    st.divider()

    option = st.selectbox(
        "Wind assisted device:",
        ("Wing", "Rotor", "Sail", "Kite"),
    )

    st.divider()

    pref_ports = [
        "Abidjan", "Bergen", "Busan", "Constanta",
        "Gdansk", "Hong Kong", "Jeddah", "Los Angeles",
        "Marseille", "Miami", "Mumbai", "New York",
        "Ras Tanura", "Rotterdam", "Sao Paulo", "Shanghai",
        "Singapore", "Sydney", "Tokyo", "Trieste", "Turku",
    ]

    tab1, tab2 = st.tabs(["Origin", "Destination"])

    with tab1:
        origin = st.selectbox(
            "Select port of origin:",
            pref_ports
        )
    with tab2:
        dest = st.selectbox(
            "Select port of destination:",
            pref_ports
        )

    import searoute as sr

    #Define origin and destination points:
    origin = [0.3515625, 50.064191736659104]

    destination = [117.42187500000001, 39.36827914916014]


    route = sr.searoute(origin, destination)
    # > Returns a GeoJSON LineString Feature
    # show route distance with unit
    st.write("{:.1f} {}".format(route.properties['length'], route.properties['units']))

    toto = route.geometry['coordinates']
    st.write(toto[0])
    st.write(type(toto[0]))
    
    import pandas as pd
    import numpy as np

    #df = pd.DataFrame(
    #    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #    columns=["lat", "lon"],
    #)
    #st.map(df)

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
