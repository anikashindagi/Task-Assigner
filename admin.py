import streamlit as st
import json
import os

TASKS_FILE = "tasks.json"
def savetasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(st.session_state.user_tasks, f)

def loadtasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            st.session_state.user_tasks = json.load(f)
    except FileNotFoundError:
        st.session_state.user_tasks = {}

def admin_page():
    st.title("Welcome Admin")
    st.write("You can now assign tasks!")
    if 'user_tasks' not in st.session_state:
        loadtasks()
    if 'user_accounts' not in st.session_state:
        st.session_state.user_accounts = [{"username": "user1"}, {"username": "user2"}]  # Example users

    st.header("Registered Users are displayed bellow-")
    if st.session_state.user_accounts:
        selected_user = st.radio('Select the user to assign the task to:', [user['username'] for user in st.session_state.user_accounts])
        task = st.text_area("Enter task for the selected user:")

        if st.button("Assign Task"):
            if selected_user in st.session_state.user_tasks:
                st.session_state.user_tasks[selected_user].append(task)
            else:
                st.session_state.user_tasks[selected_user] = [task]
            savetasks()
            st.success(f"Task assigned to {selected_user}")

    else:
        st.write("No regular users registered.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.experimental_rerun()
