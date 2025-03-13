import streamlit as st

import numpy as np
import plotly.graph_objects as go
from astropy import units as u

from pyholtrop import holtrop, read_ship
from pyresis import ship, read_ship
import waps

st.write("# Welcome to winship! 👋")

st.markdown(
    """
    A program that estimates the performance of a ship equipped with wind powered devices in 3 simple steps: select ship type & size, choose device configuration and select a course.

    Accurate results plus a graphical output will be available in just a few seconds.

    The code works by balancing the aerodynamic and hydrodynamic forces of the ship. It takes into account the most important eﬀects of the wind powered devices to predict the ship speeds at various wind conditions.

    By determining the elapsed time around the course, a direct measure of the fuel and emission savings can be assessed.
    """
)

import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from mycomponent import mycomponent
import codecs

# ---- PROJECTS SLIDESHOW FUNCTION ----
def st_slideshow(photoslider_html, height=300):
    slideshow_file = codecs.open(photoslider_html, 'r')
    page = slideshow_file.read()
    com.html(page, height=height)
    
# ---- MAIN FUNCTION ----
def main():
    #---- ONGOING PROJECTS ----
    st.markdown("**Ongoing Projects**")
    #slider_value = st_slideshow("projects/index.html")
    # Initial slider value (50 in this example)
    slider_value = mycomponent(my_input_value=50)
    
    # Display the slider value in Streamlit
    st.write("Slider Value:", slider_value)
    #value = mycomponent(my_input_value=0, key="slider")
    #st.write("Received", value)

if __name__=='__main__':
    main()

option = st.selectbox("Ship type:", 
  ("Cargo", "Container", "Passenger", "Frigate"))

file_name = option.lower() + ".shp"
#file_path = “examples/” + file_name

#out = read_ship.ReadShip(file_name)
#ship = holtrop.Holtrop(**out.ship)

out = read_ship.open(file_name)
ship = ship.Ship(*out.values())

st.slider("Length (m):", min_value=0., max_value=130., 
          value=ship.length, disabled=True)

option = st.selectbox("Waps type:", 
  ("Wing", "Rotor", "Sail", "Kite"))

file_name = option.lower() + ".dat"

waps = waps.Waps(150.)

#for AWA in range(0, 180, 10):
#    toto = waps.force(file_name, 10., AWA)
#    st.write(toto)

# Use a maritime network geograph
from scgraph.geographs.marnet import marnet_geograph

# Get the shortest path between 
output = marnet_geograph.get_shortest_path(
    origin_node={"latitude": 31.23,"longitude": 121.47}, 
    destination_node={"latitude": 32.08,"longitude": -81.09}
)

# Show your output path
st.write(str([[i['latitude'],i['longitude']] for i in output['coordinate_path']]))

# Show the length
st.write('Length: ',output['length']) #=> Length:  19596.4653
    
data = np.array(
    [
        (speed, ship.resistance(speed) / 1000.0)
        for speed in np.arange(0.1, 35.0, 0.5)
    ],
)

trace12=go.Scatter(x=data[:, 0], y=data[:, 1], mode="lines", line=dict(color="red",width=10))
fig2=go.Figure(data=trace12)
fig2.update_xaxes(title="Speed (m/s)")
fig2.update_yaxes(title="Resistance (kN)")
st.plotly_chart(fig2)
