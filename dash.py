import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def app():
 st.title('About PORTAL-')
 st.write("We are an interactive website, that allows professional conversations between the employees-Users and the supervisors-Admins.")
 st.write("We have 2 functionalities:")
 st.write("---")
 col1,col2=st.columns(2)
 with col1:
     st.write("-ADMIN-")
     st.write("Assign tasks to Users")
 with col2:
     st.write("-USERS-")
     st.write("Look at the assigned tasks and delete them if done.")
     
 lott = load_lottie("https://lottie.host/41a056a2-dbbc-4e3c-85c4-671f707d690f/UOPPpnUpvZ.json")
 column1, column2, col3 = st.columns([1,2,1])

 with column2:
    st_lottie(
        lott,
        speed=1,
        loop=True,
        quality="low",  # medium ; high
        height=300,
        width=380,
        key="lottie"
    )
