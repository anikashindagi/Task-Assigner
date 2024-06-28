# main.py
import streamlit as st
import json
import os
from admin import admin_page
from user import user_page

CREDENTIALS_FILE = "credentials.json"

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    return {"admin_accounts": [], "user_accounts": []}

def save_credentials():
    credentials = {
        "admin_accounts": st.session_state.admin_accounts,
        "user_accounts": st.session_state.user_accounts
    }
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials, f)

if 'credentials_loaded' not in st.session_state:
    credentials = load_credentials()
    st.session_state.admin_accounts = credentials["admin_accounts"]
    st.session_state.user_accounts = credentials["user_accounts"]
    st.session_state.credentials_loaded = True

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0


def login_signup():
    st.title("Login/Signup Page")
    columnn,columnnn=st.columns(2)
    with columnn:
     st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
     role = st.radio("Select role:", ("Admin", "User"))
    with columnnn:
     st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
     action = st.radio("Choose action:", ("Login", "Sign Up"))

    if action == "Sign Up":
        username = st.text_input("Create Username")
        password = st.text_input("Create Password", type="password")
        
        if role == "Admin":
            admin_key = st.text_input("Enter Admin Key")
            if st.button("Sign Up"):
                if username and password and admin_key == "ADMIN1":
                    st.session_state.admin_accounts.append({"username": username, "password": password})
                    save_credentials()
                    st.success("Admin account created successfully!")
                else:
                    st.error("Invalid admin key or missing information.")
        else:
            if st.button("Sign Up"):
                if username and password:
                    st.session_state.user_accounts.append({"username": username, "password": password})
                    save_credentials()
                    st.success("User account created successfully!")
                else:
                    st.error("Please fill all fields.")

    else:  
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if role == "Admin":
                if any(admin["username"] == username and admin["password"] == password for admin in st.session_state.admin_accounts):
                    st.session_state.logged_in = True
                    st.session_state.user_role = "Admin"
                    st.success("Admin logged in successfully!")
                    nextpage()
                    if st.session_state.page==1:
                     main()
                else:
                    
                    st.error("Invalid admin credentials.")
                    restart()
                    if st.session_state.page ==0:
                        login_signup()
            else:
                if any(user["username"] == username and user["password"] == password for user in st.session_state.user_accounts):
                    st.session_state.logged_in = True
                    st.session_state.user_role = "User"
                    st.success("User logged in successfully!")
                    nextpage()
                    if st.session_state.page==1:
                     main()
                else:
                    st.error("Invalid user credentials.")
                    restart()
                    if st.session_state.page==0:
                      login_signup()
def main():
    if not st.session_state.logged_in:
        login_signup()
    elif st.session_state.user_role == "Admin":
        admin_page()
    elif st.session_state.user_role == "User":
        user_page()

if __name__ == "__main__":
    main()