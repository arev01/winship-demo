import streamlit as st
from contextlib import contextmanager

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
        justify-content: flex-end;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        height: 20px;
        width: 20px;
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

import numpy as np

@st.dialog("⚡ Savings", width="large")
def predict(varA, varB):
    if 'ship' not in st.session_state:
        st.error("No ship selected")
    elif 'wind' not in st.session_state:
        st.error("No device selected")
    elif 'wind_data' not in st.session_state:
        st.error("No route created")
    else:
        resistance = st.session_state['ship'].resistance / 1000
        ref_power = st.session_state['ship'].propulsion_power() / 1000
        distance = st.session_state['wind_data']['DIST'].sum()
        speed = st.session_state['ship'].speed * 1.944
        ref_energy = ref_power * distance / speed
        ref_fuel = ref_energy * 155. / 900.
        ref_emissions = ref_fuel * 900. * 3.206 / 1000000
        #st.write("Resistance: " + "{:.1f}".format(resistance) + " kN")
        #st.write("Power: " + "{:.1f}".format(ref_power) + " kW")
        #st.write("Distance: " + "{:.1f}".format(distance) + " km")
        #st.write("Speed: " + "{:.1f}".format(speed) + " km/h")
        #st.write("Energy wo/: " + "{:.1f}".format(ref_energy) + " kWh")
        #st.write("Fuel cons. wo/: " + "{:.f}".format(ref_fuel) + " L")

        genre = st.radio(
            "Choose type:",
            ["True wind", "Apparent wind"]
        )
        
        new_energy = 0
        lst_speed, lst_angle, lst_frequency = ([] for i in range(3))
        for idx, row in st.session_state['wind_data'].iterrows():
            if genre == "True wind":
                distance, wind_speed, wind_angle, _, _ = row.values.tolist()
            else:
                distance, _, _, wind_speed, wind_angle, = row.values.tolist()

            #frequency = distance / st.session_state['wind_data']['DIST'].sum()

            lst_speed.append(wind_speed)
            lst_angle.append(wind_angle)
            #lst_frequency.append(frequency)
            
            #st.write("Distance: " + str(distance) + " km")
            #st.write("Wind speed: " + str(wind_speed * 3.6) + " km/h")
            #st.write("Wind angle: " + str(wind_angle * 180. / np.pi) + " deg")
            #st.write("Wind load: " + str(st.session_state['wind'].aero_force(wind_speed, wind_angle) / 1000) + " kN")
            
            wind_load = st.session_state['wind'].aero_force(wind_speed, wind_angle)
            new_energy += st.session_state['ship'].propulsion_power(external_force=-wind_load) / 1000 * distance / speed
            
        import pandas as pd
        import plotly.express as px
        
        d = {'speed': lst_speed, 'dir': lst_angle}
        df = pd.DataFrame(data=d)

        # populate values in new columns
        df['dirDeg'] = df['dir'] * 180. / np.pi #+ 180.
        df['speedKt'] = df['speed'] * 1.944
        bins = [-1, 5, 10, 15, 25, np.inf]
        names = ['0-5 kt', '5-10 kt', '10-15 kt', '15-25 kt', '>25 kt']
        df['speedKtRange'] = pd.cut(df['speedKt'], bins, labels=names)

        bins = np.linspace(0, 360, 17) + 11.25
        bins = np.insert(bins, 0, 0)
        names = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW', 'N2']
        df['dirDegRange'] = pd.cut(df['dirDeg'], bins, labels=names)
        df['dirDegRange'] = df['dirDegRange'].replace('N2', 'N')

        grp = df.groupby(["dirDegRange","speedKtRange"]).size()\
                    .reset_index(name="frequency")

        grp['percentage'] = grp['frequency']/grp['frequency'].sum()*100

        fig = px.bar_polar(grp, r="percentage",
            theta="dirDegRange", color="speedKtRange",
            template="plotly_dark",
            color_discrete_sequence= ['#482878','#31688e','#1f9e89','#6ece58','#fde725'])

        fig.update_layout(polar_radialaxis_ticksuffix='%')
                        #polar_angularaxis_ticks=np.linspace(0, 360, num=16, endpoint=False))

        st.plotly_chart(fig)

        
        diff_energy = ref_energy - new_energy
        pc_energy = diff_energy / ref_energy * 100.
        new_fuel = new_energy * 155. / 900.
        diff_fuel = ref_fuel - new_fuel
        pc_fuel = diff_fuel / ref_fuel * 100.
        new_emissions = new_fuel * 900. * 3.206 / 1000000
        diff_emissions = ref_emissions - new_emissions
        pc_emissions = diff_emissions / ref_emissions * 100.
        #st.write("Energy w/: " + str(new_energy) + " kWh")
        #st.write("Fuel cons. w/: " + str(new_fuel) + " L")
        #st.write("Emissions w/: " + str(new_emissions) + " TCO2")

        if genre == "Apparent wind":
            col1, col2, col3 = st.columns(3)
            col1.metric("Power savings", '{0:,.0f} kWh'.format(diff_energy), '{0:.1f} %'.format(pc_energy))
            col2.metric("Fuel savings", '{0:,.0f} L'.format(diff_fuel), '{0:.1f} %'.format(pc_fuel))
            col3.metric("Emission savings", '{0:,.0f} TCO2e'.format(diff_emissions), '{0:.1f} %'.format(pc_emissions))

@st.dialog("🧭 Navigation", width="large")
def help():
    st.markdown(
        """
        Use the buttons at the top to go through the different steps...
        
        :material/sailing: Choose ship type. Use arrows or swipe left/right.
        
        :material/air: Choose wind device. Select image to show more information.
        
        :material/route: Create shortest route. Choose ports of origin and destination.
        
        ... and press :material/bolt: to estimate the savings.
        
        Click :material/explore: to show this page.
        """
    )

# Button to switch page
def menu(counter):
    if counter == None:
        counter = 0
    page_lst = [
        "./pages/page_1.py",
        "./pages/page_2.py",
        "./pages/page_3.py"
    ]
    with st_horizontal():
        if st.button(":material/sailing:"):
            st.switch_page("./pages/page_1.py")
        if st.button(":material/air:"):
            st.switch_page("./pages/page_2.py")
        if st.button(":material/route:"):
            st.switch_page("./pages/page_3.py")
        if st.button(":material/bolt:"):
            predict(42, 12)
        if st.button(":material/explore:"):
            help()
        #if st.button(":material/home:"):
        #    counter = 0
        #    page_file = "./streamlit_app.py"
        #    # Switch to the selected page
        #    st.switch_page(page_file)
        #if st.button(":material/arrow_back_ios:"):
        #    counter -= 1
        #    page_file = page_lst[counter-1]
            # Switch to the selected page
        #    st.switch_page(page_file)
        #if st.button(":material/arrow_forward_ios:"):
        #    counter += 1
        #    counter = counter % 3
        #    page_file = page_lst[counter-1]
        #    # Switch to the selected page
        #    st.switch_page(page_file)

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
        case "suction":
            st.write("""A thick profile wing with internal fans 
            to reduce flow separation and thus generate higher lift.""")
        case "wing":
            st.write("""A rigid aerofoil shape mounted vertically 
            on the ship to provide a propulsive force.""")
        case "sail":
            st.write("""A traditional concept using new, 
            robust materials and automated control systems.""")
        case "kite":
            st.write("""A gigantic rig deployed above the ship 
            to assist in pulling the ship through the water.""")
