"""
Retriever utilities for the RAG pipeline.
"""

import chromadb
from typing import Any, cast

from app.rag.embeddings import get_embedding_model

from config import (
    VECTOR_DB_DIR,
    COLLECTION_NAME,
    DEFAULT_TOP_K,
)

# Initialize once
client = chromadb.PersistentClient(
    path=VECTOR_DB_DIR
)

collection = client.get_collection(
    name=COLLECTION_NAME
)

embedding_model = get_embedding_model()


def retrieve(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    category: str | None = None
) -> dict[str, Any]:
    """
    Retrieve relevant chunks for a query.

    Args:
        query:
            Search query.

        top_k:
            Number of results.

        category:
            Optional metadata category filter.

    Returns:
        Chroma query results.
    """

    query_embedding = embedding_model.embed_query(
        query
    )

    query_params = {
        "query_embeddings": [
            query_embedding
        ],
        "n_results": top_k
    }

    if category:
        query_params["where"] = {
            "category": category
        }

    results = collection.query(
        **query_params
    )

    return cast(dict[str, Any], results)