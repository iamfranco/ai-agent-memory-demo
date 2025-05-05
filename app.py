import streamlit as st
from ui_components.sidebar import sidebar
from ui_components.pages.chat_page import chat_page
from ui_components.pages.vector_db_page import vector_db_page

st.set_page_config(layout="wide")

def _pages_links():
  pg = st.navigation([
    st.Page(chat_page, title="Chat", icon="💬"),
    st.Page(vector_db_page, title="Knowledge Base", icon="📚"), 
  ])
  pg.run()

sidebar()
_pages_links()