from dotenv import load_dotenv

load_dotenv()

from src.vector_store import init_vector_store

init_vector_store()


import chainlit as cl
from src.bot import chain


@cl.on_chat_start
def main():
    cl.user_session.set("llm_chain", chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["answer"]).send()
