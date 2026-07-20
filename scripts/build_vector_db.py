"""
Build the Chroma vector database.

Pipeline:

Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
ChromaDB
"""

import chromadb

from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.embeddings import get_embedding_model


KNOWLEDGE_PATH = "knowledge"
VECTOR_DB_DIR = "vector_db"
COLLECTION_NAME = "career_docs"


def main():

    print("\nLoading documents...")

    documents = load_documents(
        KNOWLEDGE_PATH
    )

    print(
        f"Documents loaded: {len(documents)}"
    )


    print("\nSplitting documents...")

    chunks = split_documents(
        documents
    )

    print(
        f"Chunks created: {len(chunks)}"
    )


    print("\nLoading embedding model...")

    embedding_model = get_embedding_model()


    print("\nGenerating embeddings...")

    texts = [
        chunk.text
        for chunk in chunks
    ]

    embeddings = embedding_model.embed_documents(
        texts
    )


    print("\nInitializing Chroma...")

    client = chromadb.PersistentClient(
        path=VECTOR_DB_DIR
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )


    print("\nStoring vectors...")

    for index, chunk in enumerate(chunks):

        collection.add(
            ids=[
                f"chunk_{index}"
            ],
            documents=[
                chunk.text
            ],
            embeddings=[
                embeddings[index]
            ],
            metadatas=[
                {
                    "source": chunk.source,
                    "category": chunk.category,
                    "chunk_number": chunk.chunk_number
                }
            ]
        )


    print("\n==============================")
    print("Vector Database Complete")
    print("==============================")
    print(
        f"Chunks stored: {len(chunks)}"
    )
    print(
        f"Database location: {VECTOR_DB_DIR}"
    )


if __name__ == "__main__":
    main()