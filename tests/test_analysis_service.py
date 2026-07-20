from pathlib import Path

from app.services.analysis_service import AnalysisService


def test_analysis_service(tmp_path: Path):

    resume_file = tmp_path / "resume.txt"

    resume_file.write_text(
        """
        Python
        AWS
        Docker
        """,
        encoding="utf-8",
    )

    job_file = tmp_path / "job.txt"

    job_file.write_text(
        """
        Python
        AWS
        Terraform
        """,
        encoding="utf-8",
    )

    service = AnalysisService()

    context = service.analyze(
        str(resume_file),
        str(job_file),
    )

    assert context.resume is not None

    assert context.job_description is not None

    assert context.ats_result is not None

    assert "python" in (
        context.ats_result.matched_skills
    )

    assert "terraform" in (
        context.ats_result.missing_skills
    )