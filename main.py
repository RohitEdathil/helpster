from dotenv import load_dotenv

load_dotenv()

from src.vector_store import init_vector_store

init_vector_store()

from src.chat_ui import init_ui

init_ui()

from src.bot import get_reply
import streamlit as st
from src.message_model import Message

# Accept user input
if prompt := st.chat_input("Ask away!"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append(Message("user", prompt))

    reply = get_reply(prompt)

    # Display bot message in chat message container
    with st.chat_message("assistant"):
        st.markdown(reply)
    # Add bot message to chat history
    st.session_state.messages.append(Message("assistant", reply))
