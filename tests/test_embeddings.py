from app.rag.embeddings import get_embedding_model


def test_embedding_creation():

    embeddings = get_embedding_model()

    result = embeddings.embed_query(
        "ATS resume optimization strategies"
    )

    assert len(result) > 0

    print(
        f"\nEmbedding dimensions: {len(result)}"
    )