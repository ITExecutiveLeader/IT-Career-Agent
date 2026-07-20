"""
Embedding utilities for the RAG pipeline.

Uses Ollama local embedding models.
"""

from langchain_ollama import OllamaEmbeddings

from config import EMBEDDING_MODEL


# Cached singleton instance
_embedding_model = None


def get_embedding_model() -> OllamaEmbeddings:
    """
    Return the shared local embedding model.

    The embedding model is created only once and reused throughout
    the application.
    """
    global _embedding_model

    if _embedding_model is None:
        _embedding_model = OllamaEmbeddings(
            model=EMBEDDING_MODEL
        )

    return _embedding_model