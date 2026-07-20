from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents


def main():

    documents = load_documents("knowledge")

    chunks = split_documents(documents)

    print(f"Total chunks: {len(chunks)}")

    first_chunk = chunks[0]

    print("\nFirst Chunk\n")

    print(first_chunk.source)
    print(first_chunk.category)
    print(first_chunk.chunk_number)

    print("\nPreview:\n")

    print(first_chunk.text[:500])


if __name__ == "__main__":
    main()