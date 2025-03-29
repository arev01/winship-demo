import streamlit as st

def prompt(person):
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
        case "rotor":
            st.write("""A rotating cylinder that generates lift 
            at right angles to the wind to drive the ship forward.""")
        case "wing":
            st.write("""A rigid aerofoil shape mounted vertically 
            on the ship to provide a propulsive force.""")
        case "sail":
            st.write("""A traditional concept using new, 
            robust materials and automated control systems.""")
        case "kite":
            st.write("""A gigantic rig deployed above the ship 
            to assist in pulling the ship through the water.""")
