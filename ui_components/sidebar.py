import streamlit as st

def sidebar():
  with st.sidebar:
    if not st.user.is_logged_in:
      st.button("Log in with Google", on_click=st.login)
    else:
      st.button("Log out", on_click=st.logout)
      st.image(st.user.picture)
      st.write(st.user.name)