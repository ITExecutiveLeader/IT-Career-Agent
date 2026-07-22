from pathlib import Path
import tempfile
import fitz

with tempfile.TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "bad.pdf"
    path.write_bytes(b"this is not a valid pdf")

    try:
        pdf_bytes = path.read_bytes()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf",
        )
    except Exception as e:
        print("Expected:", e)

    print("About to exit TemporaryDirectory...")