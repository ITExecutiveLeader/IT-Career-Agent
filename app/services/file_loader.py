"""
Utility for loading a single document.
"""

from pathlib import Path

import fitz


class FileLoader:
    """
    Loads a single document into plain text.
    """

    def load(self, file_path: str) -> str:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return self._load_pdf(path)

        if suffix == ".txt":
            return path.read_text(encoding="utf-8")

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )
    

    @staticmethod
    def _load_pdf(path: Path) -> str:
        try:
            pdf_bytes = path.read_bytes()

            doc = fitz.open(
                stream=pdf_bytes,
                filetype="pdf",
            )

            try:
                pages = []

                for page in doc:
                    page_text = page.get_text("text")

                    if isinstance(page_text, str):
                        pages.append(page_text)

                return "\n".join(pages).strip()

            finally:
                doc.close()

        except Exception as exc:
            raise ValueError(
                f"Unable to read PDF file: {path}"
            ) from exc