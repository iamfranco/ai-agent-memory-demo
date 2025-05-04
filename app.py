import streamlit as st

if not st.user.is_logged_in:
  st.button("Log in with Google", on_click=st.login)
else:
  st.user
  st.button("Log out", on_click=st.logout)