import streamlit as st
from mycomponent import mycomponent

# ---- MAIN FUNCTION ----
def main():
    #---- ONGOING PROJECTS ----
    st.write("# Welcome to winship! 👋")
    out = mycomponent(my_input_value=50)
    
    # Display the output in Streamlit
    st.write("Ship type:", out.capitalize())

    option = st.selectbox(
        "Wind assisted device:",
        ("Wing", "Rotor", "Sail", "Kite"),
    )

    st.write("You selected:", option)

    def reset():
        st.session_state.selection = 'Please Select'

    route = st.selectbox(
        "Start/end port:",
        ("Abidjan", "Bergen", "Busan", "Constanta",
         "Gdansk", "Hong Kong", "Jeddah", "Los Angeles",
         "Marseille", "Miami", "Mumbai", "New York",
         "Ras Tanura", "Rotterdam", "Sao Paulo", "Shanghai",
         "Singapore", "Sydney", "Tokyo", "Trieste", "Turku"),
        index=None,
        placeholder="Please select",
        key='selection',
        on_click=reset,
    )

    st.write("You selected:", route)

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])  # Adjust column ratios as needed

    with col1:
        if st.button("Spring"):
            st.write("Spring selected")

    with col2:
        if st.button("Summer"):
            st.write("Summer selected")

    with col3:
        if st.button("Autumn"):
            st.write("Autumn selected")

    with col4:
        if st.button("Winter"):
            st.write("Winter selected")

    with col5:
        if st.button("All year"):
            st.write("All year selected")

if __name__=='__main__':
    main()
