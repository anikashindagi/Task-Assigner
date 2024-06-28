import streamlit as st
from streamlit_option_menu import option_menu
import login
import dash

st.set_page_config(page_title="PORTAL!",page_icon=':blue heart:',layout="wide")

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title='PORTAL',
            options=['Login/Signup','Dashboard'],
            icons=['key','book'],
            default_index=0,
        )
        
    if selected == "Login/Signup":
        login.login_signup()
    if selected == "Dashboard":
        dash.app()
  
if __name__ == "__main__":
    main()