"""
Shared service for retrieving knowledge from the vector database.
"""

from app.rag.retriever import retrieve


class RAGService:
    """Application service for knowledge retrieval."""

    def search(
        self,
        query: str,
        category: str | None = None,
        top_k: int = 3,
    ) -> str:

        results = retrieve(
            query=query,
            top_k=top_k,
            category=category,
        )

        output = []

        for document, metadata in zip(
            results["documents"][0],
            results["metadatas"][0],
        ):
            output.append(
                f"""
Source:
{metadata['source']}

Content:
{document}
"""
            )

        return "\n\n".join(output)