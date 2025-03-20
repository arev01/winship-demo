import streamlit as st
from mycomponent import mycomponent
from functions import greet
from navigation import menu

menu(counter=2)

option = st.segmented_control("Wind assisted device:",
    ["Rotor", "Suction", "Wing", "Sail", "Kite"],
)

with st.container(height=393, border=True):
    cols_mr = st.columns([10.9, 0.2, 10.9])
    with cols_mr[0].container(height=350, border=False):
        st.write("Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. Build and deploy powerful data apps in minutes. Let's get started!")
        st.image("./img/" + option.lower() + ".jpg")
    with cols_mr[1]:
        st.html(
            '''
                <div class="divider-vertical-line"></div>
                <style>
                    .divider-vertical-line {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        height: 320px;
                        margin: auto;
                    }
                </style>
            '''
        )
    with cols_mr[2].container(height=350, border=False):
        greet(option.lower())
