from app.rag.retriever import retrieve


def test_category_filter():

    results = retrieve(
        "resume formatting",
        top_k=3,
        category="ats_guides"
    )

    assert results["documents"]

    for metadata in results["metadatas"][0]:
        assert metadata["category"] == "ats_guides"