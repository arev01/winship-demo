import streamlit as st
from functions import menu, prompt

menu(counter=3)

st.markdown("### (3/3) Select a route")

import xarray as xr
import numpy as np
import pandas as pd

# Open the ERA-5 data
data = xr.open_dataset('ERA5.nc')

# Define latitude and longitude coordinates
lat = data.latitude[::3]
lat = lat.sortby(lat)
lon = data.longitude[::3] - 180.

# Define the u-, v- wind speeds
wind_u = data.u[:,0,::3,::3].mean(axis=0)
wind_v = data.v[:,0,::3,::3].mean(axis=0)

def find_index(x, y):
    global lat, lon
    xi = np.searchsorted(lat, x)-1
    yi = np.searchsorted(lon, y)-1
    return xi, yi

from nodes import nodes

#Define origin and destination ports
tab1, tab2 = st.tabs(["Origin", "Destination"])
values = ['<select>', *nodes.keys()]

with tab1:
    origin = st.selectbox(
        "Select port of origin:",
        values
    )
with tab2:
    destination = st.selectbox(
        "Select port of destination:",
        values
    )

# Use a maritime network geograph
from scgraph.geographs.marnet import marnet_geograph

col = ["latitude", "longitude"]

if origin != '<select>' and destination != '<select>':
    # Get the shortest path between 
    marnet_output = marnet_geograph.get_shortest_path(
        origin_node = {col[i]: nodes[origin][i] for i, _ in enumerate(col)},
        destination_node = {col[i]: nodes[destination][i] for i, _ in enumerate(col)},
        output_units = "km"
    )
    st.write("Distance: " + str(marnet_output['length']) + " km")

    df = pd.DataFrame(
        #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        marnet_output['coordinate_path'],
        columns = col,
    )
    st.map(df, height=300)

    st.toggle("Show wind", disabled=True, help="Currently unavailable")

    from pyaero import navigation

    lst = []
    for i in range(len(marnet_output['coordinate_path'])-1):
        p1 = marnet_output['coordinate_path'][i]
        p2 = marnet_output['coordinate_path'][i+1]

        if p2[1] == p1[1] and p2[0] > p1[0]:
            boat_u = 0.
            boat_v = st.session_state['ship'].speed1
        elif p2[1] == p1[1] and p2[0] < p1[0]:
            boat_u = 0.
            boat_v = -1. * st.session_state['ship'].speed1
        else:
            X = ( p2[0] - p1[0] ) / ( p2[1] - p1[1] )
            boat_u = -1. * st.session_state['ship'].speed1 / np.sqrt(1 + X**2) * X
            boat_v = st.session_state['ship'].speed1 / np.sqrt(1 + X**2)

        xi, yi = find_index(*p1)

        #st.write(*p1)
        #st.write(xi, yi)
        #st.write(lat.item(xi), lon.item(yi))
        #st.write(wind_u.shape)
        #st.write(wind_u[xi, yi])

        # Construct speed vectors
        v0 = np.asarray([boat_u, boat_v], dtype=float)
        v1 = np.asarray([wind_u[xi, yi], wind_v[xi, yi]], dtype=float)

        st.write("v0: ", *v0)
        st.write("v1: ", *v1)
        tws, twa, aws, awa = navigation.velocity(v0, v1)
        st.write("aws: ", aws)
        st.write("awa: ", awa * 180. / np.pi)
        st.write()
    
        lst.append([navigation.distance(*p1, *p2), *navigation.velocity(v0, v1)])
    
    wind_data = pd.DataFrame(lst, columns=['DIST', 'TWS', 'TWA', 'AWS', 'AWA'])
    st.session_state['wind_data'] = wind_data
