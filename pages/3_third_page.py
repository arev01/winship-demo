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

import xarray as xr

# Open the ERA-5 data
data = xr.open_dataset('ERA5.nc')

# Define latitude and longitude coordinates
x = data.latitude[::3]
y = data.longitude[::3]

import pandas as pd
import numpy as np

# Define the u-, v- wind speeds
wind_u = np.asarray(data.u[0,0,::3,::3], dtype=float)
wind_v = np.asarray(data.v[0,0,::3,::3], dtype=float)

xx, yy = np.meshgrid(x, y)
coords = np.c_[xx.ravel(), yy.ravel(), wind_u.ravel(), wind_v.ravel()]

#DATA_SOURCE = pd.DataFrame(wind_u, wind_v, index=lat, columns=lon)

#DATA_SOURCE = DATA_SOURCE.unstack()

from scipy import interpolate

itp = interpolate.RegularGridInterpolator( (x, y), wind_u, method='nearest') 
res = itp([89.99, 0.31])
st.write(res)

#for i in range(len(marnet_output['coordinate_path'])-1):
#    first_node = marnet_output['coordinate_path'][i]
#    second_node = marnet_output['coordinate_path'][i+1]

# Get the magnitude of wind speed
#WS = np.sqrt(wind_u **2 + wind_v **2)

df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    marnet_output['coordinate_path'],
    columns = col,
)
st.map(df, height=300)

st.toggle("Show wind", disabled=True, help="Currently unavailable")
