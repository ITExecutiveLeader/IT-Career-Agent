"""
Split loaded documents into overlapping chunks for embedding.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.models import Document, Chunk


def split_documents(
    documents: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[Chunk]:
    """
    Split documents into overlapping text chunks.

    Args:
        documents:
            Documents to split.

        chunk_size:
            Maximum characters per chunk.

        chunk_overlap:
            Characters shared between neighboring chunks.

    Returns:
        List of Chunk objects.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks: list[Chunk] = []

    for document in documents:

        pieces = splitter.split_text(document.text)

        for index, piece in enumerate(pieces, start=1):

            chunks.append(
                Chunk(
                    text=piece,
                    source=document.source,
                    category=document.category,
                    chunk_number=index
                )
            )

    print(f"\nCreated {len(chunks)} chunk(s).\n")

    return chunks