from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents


def test_chunk_quality():

    documents = load_documents("knowledge")

    chunks = split_documents(documents)

    bad_chunks = []

    for chunk in chunks:
        if len(chunk.text.strip()) < 100:
            bad_chunks.append(chunk)

    assert len(bad_chunks) == 0, (
        f"Found {len(bad_chunks)} low quality chunks: "
        f"{[chunk.source for chunk in bad_chunks]}"
    )