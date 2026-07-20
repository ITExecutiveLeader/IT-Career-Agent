from app.tools import search_resume_knowledge


def test_rag_tool():

    result = search_resume_knowledge.run(
        "What are ATS resume formatting best practices?"
    )

    print("\nRAG TOOL RESULT:\n")
    print(result[:1000])

    assert result
    assert "ATS" in result or "resume" in result.lower()