import streamlit as st

from models.chat_message import ChatMessage, get_avatar

def initialize_chat_messages():
  if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

def show_single_chat_message(chat_message: ChatMessage):
  st.chat_message(
    chat_message.role, 
    avatar=get_avatar(chat_message.role)
  ).markdown(chat_message.message)

def show_and_append_single_chat_message(chat_message: ChatMessage):
  show_single_chat_message(chat_message)
  initialize_chat_messages()
  st.session_state.chat_messages.append(chat_message)

def show_chat_messages():
  initialize_chat_messages()
  for chat_message in st.session_state.chat_messages:
    show_single_chat_message(chat_message)
