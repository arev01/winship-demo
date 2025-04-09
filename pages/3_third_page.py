import streamlit as st
from functions import menu, prompt

menu(counter=3)

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

col = ["latitude", "longitude"]

# Get the shortest path between 
marnet_output = marnet_geograph.get_shortest_path(
    origin_node = {col[i]: nodes[origin][i] for i, _ in enumerate(col)},
    destination_node = {col[i]: nodes[destination][i] for i, _ in enumerate(col)},
    output_units = "km"
)
st.write("Distance: " + str(marnet_output['length']) + " km")

import pandas as pd

df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    marnet_output['coordinate_path'],
    columns = col,
)
st.map(df, height=300)

st.toggle("Show wind", disabled=True, help="Currently unavailable")

import xarray as xr
import numpy as np

# Open the ERA-5 data
data = xr.open_dataset('ERA5.nc')

# Define latitude and longitude coordinates
lat = data.latitude[::3]
lon = data.longitude[::3]

# Define the u-, v- wind speeds
wind_u = data.u[0,0,::3,::3]
wind_v = data.v[0,0,::3,::3]

def find_index(x, y):
    global lat, lon
    xi = np.searchsorted(lat, x)
    yi = np.searchsorted(lon, y)
    return xi, yi

from pyaero import navigation

wind_data = pd.DataFrame(columns=['DIST', 'TWS', 'TWA', 'AWS', 'AWA'])

for i in range(len(marnet_output['coordinate_path'])-1):
    p1 = marnet_output['coordinate_path'][i]
    p2 = marnet_output['coordinate_path'][i+1]

    if p1[0] == p2[0]:
        boat_u = st.session_state['ship'].speed1
        boat_v = 0
    else:
        X = ( p1[1] - p2[1] ) / ( p1[0] - p2[0] )
        boat_u = st.session_state['ship'].speed1 / np.sqrt(1 + X**2) * X
        boat_v = st.session_state['ship'].speed1 / np.sqrt(1 + X**2)

    xi, yi = find_index(*p1)

    # Construct speed vectors
    v0 = np.asarray([boat_u, boat_v], dtype=float)
    v1 = np.asarray([wind_u[yi, xi], wind_v[yi, xi]], dtype=float)

    distance = navigation.distance(*p1, *p2)

    wind_data.loc[-1] = [distance] + list(navigation.velocity(v0, v1))

if 'wind_data' not in st.session_state:
    st.session_state['wind_data'] = wind_data
