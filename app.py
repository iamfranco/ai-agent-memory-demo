import asyncio
import streamlit as st

from ui_components.chat_messages import show_and_append_single_chat_message, show_chat_messages
from ui_components.sidebar import sidebar
from agents.chat_agent import ChatAgent
from models.chat_message import ChatMessage

if "chat_agent" not in st.session_state:
  st.session_state.chat_agent = ChatAgent()

sidebar()
show_chat_messages()

prompt = st.chat_input("Type a message")
if prompt:
  show_and_append_single_chat_message(ChatMessage(role="user", message=prompt))

  with st.spinner("Generating response...", show_time=True):
    response = asyncio.run(st.session_state.chat_agent.chat(prompt))
    show_and_append_single_chat_message(ChatMessage(role="assistant", message=response))
