from dotenv import load_dotenv

load_dotenv()

from src.vector_store import init_vector_store
from os import listdir
from os.path import join
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from tqdm import tqdm

init_vector_store()

index = pinecone.Index("helpster")
embedding = OpenAIEmbeddings()

files = listdir("data")
for file_name in tqdm(files, total=len(files), desc="Loading"):
    # Opening file
    file = open(join("data", file_name)).read()

    # Creating vector
    vector = [
        (file_name, values, {"data": file})
        for values in embedding.embed_documents([file])
    ]
    index.upsert(vectors=vector)
