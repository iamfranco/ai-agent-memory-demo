import streamlit as st

from helpers.css_helper import apply_css

def _login_section():
  apply_css("./ui_components/style.css")

  with st.container(key="login_section"):
    if not st.user.is_logged_in:
      st.button("Log in with Google", on_click=st.login)
    else:
      st.button("Log out", on_click=st.logout)
      
      with st.container(key="user_info"):
        st.image(st.user.picture, width=30)
        st.write(st.user.name)
        

def sidebar():
  with st.sidebar:
    _login_section()
