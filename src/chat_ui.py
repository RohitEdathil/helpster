import streamlit as st
from .message_model import Message
from typing import List


def init_ui():
    st.title("Helpster")
    st.subheader("Ask me anything about AICSSYC!")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages: List[Message] = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message.role):
            st.markdown(message.content)
