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
output = marnet_geograph.get_shortest_path(
    origin_node = {col[i]: nodes[origin][i] for i, _ in enumerate(col)},
    destination_node = {col[i]: nodes[destination][i] for i, _ in enumerate(col)}
)
st.write("Distance: ",output['length'])

import xarray as xr

# Open the ERA-5 data
data = xr.open_dataset('ERA5.nc')

# Define latitude and longitude coordinates
x = data.latitude
y = data.longitude

# Define the u-, v- wind speeds
wind_u = data.u
wind_v = data.v

import pandas as pd
import numpy as np

# Get the magnitude of wind speed
WS = np.sqrt(wind_u **2 + wind_v **2)

DATA_SOURCE = pd.DataFrame(WS[0,0,:,:], index=x, columns=y)

st.write(DATA_SOURCE.shape)
df1 = DATA_SOURCE.unstack()
st.write(df1.shape)
st.write(df1)
df2 = df1.sample(frac=0.5)
st.write(df2.shape)
st.write(df2)

df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    output['coordinate_path'],
    columns = col,
)
st.map(df, height=300)
