from pinecone import init

from os import getenv


def init_vector_store():
    api_key = getenv("PINECONE_API_KEY")
    env = getenv("PINECONE_ENV")

    init(api_key=api_key, environment=env)
