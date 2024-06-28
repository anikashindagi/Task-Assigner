
import streamlit as st
import json

def savetasks():
    with open('tasks.json', 'w') as f:
        json.dump(st.session_state.user_tasks, f)

def loadtasks():
    try:
        with open('tasks.json', 'r') as f:
            st.session_state.user_tasks = json.load(f)
    except FileNotFoundError:
        st.session_state.user_tasks = {}

def user_page():
    st.title("Welcome Users!")
    st.write("You can look at your assigned tasks here and delete them if you have completed them.")
    if 'user_tasks' not in st.session_state:
        loadtasks()
    if 'current_user' not in st.session_state:
        st.session_state.current_user = ""
    if 'user_accounts' not in st.session_state:
        st.session_state.user_accounts = []
    name = st.text_input('Enter your name to view your tasks for today:')

    if st.button("View Tasks"):
        st.session_state.current_user = name

    if st.session_state.current_user in st.session_state.user_tasks:
        st.write('Your tasks are:')
        tasks = st.session_state.user_tasks[st.session_state.current_user]
        for task in tasks:
            st.write(f"- {task}")
 
    else:
        if st.session_state.current_user:
            st.write("No tasks assigned/user not found.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.experimental_rerun()
