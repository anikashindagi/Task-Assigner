import streamlit as st
from datetime import datetime

def admin_page():
    st.title("Welcome Admin-")
    st.write("You can now assign tasks!")
    # current_time = datetime.now()
    # noww= current_time.strftime("%Y-%m-%d %H:%M:%S")
    # st.write( "Current Date and Time: {time}")
    

    st.header("Registered Users--")
    if st.session_state.user_accounts:
        for user in st.session_state.user_accounts:
            st.write(f"Username: {user['username']}")
    else:
        st.write("No regular users registered.")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        from login import save_credentials
        save_credentials()
        st.experimental_rerun()