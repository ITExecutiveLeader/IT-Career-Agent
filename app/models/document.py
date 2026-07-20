"""
Document model used throughout the RAG pipeline.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    """
    Represents a knowledge document loaded from disk.
    """

    source: str
    category: str
    text: str

    @property
    def filename(self) -> str:
        """Return the filename only."""
        return self.source.replace("\\", "/").split("/")[-1]