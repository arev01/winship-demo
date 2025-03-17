import streamlit as st
from ..mycomponent import mycomponent

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

out = mycomponent(my_input_value=50)
    
# Display the output in Streamlit
st.write("You selected: ", out.capitalize())

greet(out)

option = st.selectbox(
    "Wind assisted device:",
    ("Wing", "Rotor", "Sail", "Kite"),
)

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
