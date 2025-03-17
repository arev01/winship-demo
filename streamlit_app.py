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
        /*justify-content: flex-end;*/
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

import SessionState

def pageZero(sesh):
    st.title("# Welcome to winship! 👋")
    st.write('some text for zeroth page. Welcome to the app. Follow the nav buttons above to move forward and backwards one page')

def pageOne(sesh):
    st.title('page ONE')
    out = mycomponent(my_input_value=50)
    
    # Display the output in Streamlit
    st.write("You selected: ", out.capitalize())

    greet(out)

def pageTwo(sesh):
    st.title('TWO')
    option = st.selectbox(
        "Wind assisted device:",
        ("Wing", "Rotor", "Sail", "Kite"),
    )

def pageThree(sesh):
    st.title('THREE')
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

sesh = SessionState.get(curr_page = 0)
PAGES = [pageZero, pageOne, pageTwo, pageThree]

def greet(person):
    match person:
        case "container":
            st.write("""A ship specifically designed 
            to carry dry cargo in intermodal containers.""")
        case "cargo":
            st.write("""A multi-purpose ship designed 
            to transport a wide variety of goods and commodities.""")
        case "tanker":
            st.write("""A ship specifically designed 
            to carry liquid cargo, including petroleum, chemicals 
            and pressurized gases.""")
        case "bulker":
            st.write("""A ship specifically designed 
            to transport unpackaged bulk cargo such as grain, coal, 
            ore, steel coils and cement.""")
        case "frigate":
            st.write("""A small, fast military ship used 
            to protect other ships.""")
        case "passenger":
            st.write("""A large ship designed 
            to carry people on voyages for vacationing.""")

# ---- MAIN FUNCTION ----
def main():
    st.markdown(' ### Navigation')
    st.markdown('Click Next to go to the next page')
    with st_horizontal():
        if st.button('Back:'):
            sesh.curr_page = max(0, sesh.curr_page-1)
        if st.button('Next page:'):
            sesh.curr_page = min(len(PAGES)-1, sesh.curr_page+1)
    st.markdown('----------------------------------')


    #####MAIN PAGE APP:
    st.write('PAGE NUMBER:', sesh.curr_page)
    page_turning_function = PAGES[sesh.curr_page]
    st.write(sesh.curr_page)
    page_turning_function(sesh)

if __name__=='__main__':
    main()
