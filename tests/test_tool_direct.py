from app.tools.knowledge_search import search_resume_knowledge


def test_tool_direct():

    result = search_resume_knowledge.run(
        "What are ATS resume formatting best practices?"
    )

    print("\nRESULT:")
    print(result)

    assert result