import streamlit as st
from mycomponent import mycomponent
from functions import prompt
from navigation import menu

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

# Define the u-, v- wind speeds
wind_u = data.u[0,0,::3,::3]
wind_v = data.v[0,0,::3,::3]

import pandas as pd
import numpy as np

xx, yy = np.meshgrid(x, y)
coords = np.c_[xx.ravel(), yy.ravel()]

st.write(coords.shape)
st.write(wind_u.shape)
st.write(wind_u.unstack().shape)

#d1 = np.r_[coords, wind_u.unstack()]
#st.write(d1)

# Get the magnitude of wind speed
WS = np.sqrt(wind_u **2 + wind_v **2)

DATA_SOURCE = pd.DataFrame(WS[0,0,:,:], index=x, columns=y)

# Unstack
DATA_SOURCE = DATA_SOURCE.unstack()

# Random sample
#DATA_SOURCE = DATA_SOURCE.sample(frac=0.1)

# Rename columns
DATA_SOURCE = DATA_SOURCE.reset_index().rename(columns={'level_0':'lon','level_1':'lat',0:'WS'})

st.write(DATA_SOURCE)

df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    marnet_output['coordinate_path'],
    columns = col,
)
st.map(df, height=300)

st.toggle("Show wind", disabled=True, help="Currently unavailable")
