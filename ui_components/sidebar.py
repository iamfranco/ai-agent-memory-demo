import streamlit as st

def sidebar():
  if "username" not in st.session_state:
    st.session_state.username = None

  with st.sidebar:
    if not st.user.is_logged_in:
      st.button("Log in with Google", on_click=st.login)
      st.session_state.username = None
    else:
      st.session_state.username = st.user.name
      st.button("Log out", on_click=st.logout)
      st.image(st.user.picture)
      st.write(st.user.name)