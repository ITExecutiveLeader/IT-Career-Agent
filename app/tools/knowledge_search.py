"""
CrewAI tool for searching the career knowledge base.
"""

from crewai.tools import tool

from app.services import RAGService

rag_service = RAGService()

@tool("Search Career Knowledge Base")
def search_resume_knowledge(
    query: str,
    category: str | None = None
    ) -> str:
    """
    Search resume, ATS, and career guidance documents.

    Use this tool for:
    - ATS optimization guidance
    - resume formatting rules
    - recruiter expectations
    - resume best practices
    """

    return rag_service.search(
        query=query,
        category=category,
        top_k=3,
    )