import streamlit as st

def apply_css(css_file: str):
  with open(css_file, 'r') as file:
    css = file.read()

  st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)