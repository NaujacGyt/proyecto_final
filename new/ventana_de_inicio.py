import streamlit as st
from login_cuestionario import login , signup

st.image(
    "recursos/logo_surflink.png", 
    width=300,
    caption="Python"
)
def main():

    st.title("Simple login")

    menu = ["Home", "Login", "SignUp"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        login()

    elif choice == "SignUp":
        signup()

if __name__ == "__main__":
    main()