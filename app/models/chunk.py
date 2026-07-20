"""
Chunk model used throughout the RAG pipeline.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    """
    Represents a chunk of a document that will be embedded.
    """

    text: str
    source: str
    category: str
    chunk_number: int