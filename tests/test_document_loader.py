from app.rag.document_loader import load_documents


def main():

    documents = load_documents("knowledge")

    print("\nFirst document:\n")

    document = documents[0]

    print(document.source)
    print(document.category)
    print(document.filename)
    print(document.text[:500])


if __name__ == "__main__":
    main()