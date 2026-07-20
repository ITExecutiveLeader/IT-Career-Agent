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

        pdf = fitz.open(path)

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text.strip()