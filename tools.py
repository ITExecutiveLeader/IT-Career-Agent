from pathlib import Path
from pypdf import PdfReader
from docx import Document


def read_text_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return path.read_text(encoding="utf-8")


def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def read_docx(file_path):
    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def load_document(file_path):

    extension = Path(file_path).suffix.lower()

    if extension == ".txt":
        return read_text_file(file_path)

    elif extension == ".pdf":
        return read_pdf(file_path)

    elif extension == ".docx":
        return read_docx(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )