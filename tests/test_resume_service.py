from pathlib import Path

from app.services.resume_service import ResumeService


def test_resume_service_loads_text_file(tmp_path: Path):

    resume = tmp_path / "resume.txt"

    resume.write_text(
        "John Doe\nPython Developer",
        encoding="utf-8",
    )

    service = ResumeService()

    context = service.load_resume(
        str(resume)
    )

    assert context.resume is not None

    assert context.resume.raw_text.startswith(
        "John Doe"
    )