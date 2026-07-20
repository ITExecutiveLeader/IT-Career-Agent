"""
Document loading utilities for the RAG pipeline.

This module recursively loads PDF files from the knowledge
directory and extracts their text.
"""

from pathlib import Path
import fitz  # PyMuPDF
from app.models import Document


def load_documents(knowledge_path: str) -> list[Document]:
    """
    Load all PDF documents under the knowledge directory.

    Args:
        knowledge_path:
            Root folder containing knowledge PDFs.

    Returns:
        A list of Document objects.
            - source
            - category
            - text
    """

    documents = []

    knowledge_dir = Path(knowledge_path)

    if not knowledge_dir.exists():
        raise FileNotFoundError(
            f"Knowledge directory not found: {knowledge_path}"
        )

    pdf_files = sorted(knowledge_dir.rglob("*.pdf"))

    print(f"\nFound {len(pdf_files)} PDF(s).\n")

    for pdf_path in pdf_files:

        try:
            pdf = fitz.open(pdf_path)

            text = ""

            for page in pdf:
                text += page.get_text()

            pdf.close()

            text = text.strip()

            # Skip PDFs with insufficient extracted text
            # (usually scanned images or badly formatted PDFs)
            if len(text) < 200:
                print(
                    f"Skipping low quality document: "
                    f"{pdf_path.name} ({len(text)} characters)"
                )
                continue

            documents.append(
                Document(
                    source=str(pdf_path),
                    category=pdf_path.parent.name,
                    text=text
                )
            )

            print(
                f"Loaded: {pdf_path.name} "
                f"({len(text):,} characters)"
            )

        except Exception as error:
            print(
                f"Skipping {pdf_path.name}: {error}"
            )

    print(f"\nSuccessfully loaded {len(documents)} document(s).\n")

    return documents