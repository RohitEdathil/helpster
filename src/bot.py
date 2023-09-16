from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
)
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

from pinecone import Index, list_indexes

llm = ChatOpenAI()

template = """
Answer the question in your own words as truthfully as possible from the context given to you.
If you do not know the answer to the question, simply respond with "I don't know. Can you ask another question".
If questions are asked where there is no relevant context available, simply respond with "I don't know. Please ask a question relevant to the documents"

Context: {context}

{chat_history}

Human: {question}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["context", "chat_history", "question"], template=template
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

embedding = OpenAIEmbeddings()

index = Index("helpster")

vectordb = Pinecone(
    index=index,
    embedding=embedding,
    text_key="data",
)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},
)


def get_reply(msg):
    return chain.run(msg)