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

# Random sample
DATA_SOURCE = DATA_SOURCE.sample(frac=0.1)

# Unstack
DATA_SOURCE = DATA_SOURCE.unstack()

# Rename columns
DATA_SOURCE = DATA_SOURCE.reset_index().rename(columns={'level_0':'lon','level_1':'lat',0:'WS'})

import pydeck as pdk

COLOR_BREWER_BLUE_SCALE = [
    [240, 249, 232],
    [204, 235, 197],
    [168, 221, 181],
    [123, 204, 196],
    [67, 162, 202],
    [8, 104, 172],
]

# Crate a base layer
layer = pdk.Layer(
    "HeatmapLayer",
    data=DATA_SOURCE,
    opacity=0.3,
    intensity=1,
    get_position='[long, lat]',
    aggregation=pdk.types.String("MEAN"),
    color_range=COLOR_BREWER_BLUE_SCALE,
    get_weight='WS',
)

INITIAL_VIEW_STATE = pdk.ViewState(latitude=49.254, longitude=-123.13, zoom=10.5, max_zoom=16, pitch=45, bearing=0)

# Embed the layer into pydeck object
r = pdk.Deck(layers=[layer], map_style=None)#initial_view_state=INITIAL_VIEW_STATE)

# Display the pydeck object
st.pydeck_chart(r)

df = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    output['coordinate_path'],
    columns = col,
)
st.map(df, height=300)
