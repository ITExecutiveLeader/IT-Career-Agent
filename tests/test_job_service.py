from pathlib import Path

from app.services.job_service import JobService


def test_job_service_loads_text_file(tmp_path: Path):

    job_file = tmp_path / "job.txt"

    job_file.write_text(
        "Senior Python Developer",
        encoding="utf-8",
    )

    service = JobService()

    context = service.load_job(
        str(job_file)
    )

    assert context.job_description is not None

    assert context.job_description.raw_text.startswith(
        "Senior Python"
    )