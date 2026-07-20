from app.rag.retriever import retrieve


def test_retrieval():

    results = retrieve(
        "How do I optimize a resume for an ATS?"
    )

    assert results

    print("\nRetrieved Results:\n")

    for doc, metadata in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):
        print("--------------------------------")
        print(metadata)
        print(doc[:300])