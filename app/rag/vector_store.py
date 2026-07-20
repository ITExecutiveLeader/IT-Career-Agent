"""
Vector store utilities for the RAG pipeline.

Stores document chunks using ChromaDB.
"""

from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embedding_model


VECTOR_DB_PATH = "data/chroma"


def get_vector_store():

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings,
        collection_name="career_agent_knowledge"
    )

    return vector_store