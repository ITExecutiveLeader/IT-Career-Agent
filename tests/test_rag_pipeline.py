from app.rag.retriever import retrieve


def test_rag_pipeline():

    results = retrieve(
        "What are ATS resume formatting best practices?",
        top_k=3
    )

    assert results["documents"]

    assert len(results["documents"][0]) == 3

    assert results["metadatas"]

    first_source = results["metadatas"][0][0]["source"]

    assert ".pdf" in first_source