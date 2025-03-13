import streamlit as st
from mycomponent import mycomponent

st.write("# Welcome to winship! 👋")

# ---- MAIN FUNCTION ----
def main():
    #---- ONGOING PROJECTS ----
    st.markdown("## First, select a ship type:")
    out = mycomponent(my_input_value=50)
    
    # Display the output in Streamlit
    st.write("Received:", out)

if __name__=='__main__':
    main()
