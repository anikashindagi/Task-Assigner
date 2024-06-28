# user_page.py
import streamlit as st

def user_page():
    st.title("Welcome Users!")
    st.write("You can look at your assigned tasks here and delete them if you have completed them.")
    
    
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.experimental_rerun()

