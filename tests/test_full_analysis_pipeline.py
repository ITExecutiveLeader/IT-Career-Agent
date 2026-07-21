from pathlib import Path

from app.services.analysis_service import AnalysisService


def test_full_analysis_pipeline():

    resume_path = Path("tests/data/sample_resume.pdf")
    job_path = Path("tests/data/sample_job.txt")

    assert resume_path.exists()
    assert job_path.exists()

    service = AnalysisService()

    context = service.analyze(
        resume_path=str(resume_path),
        job_path=str(job_path),
    )

    assert context is not None

    # Resume validation
    assert context.resume is not None

    assert context.resume.skills is not None
    assert len(context.resume.skills) > 0

    # Job validation
    assert context.job_description is not None

    assert context.job_description.required_skills is not None
    assert len(context.job_description.required_skills) > 0

    # ATS validation
    assert context.ats_result is not None

    # Career intelligence validation
    assert context.career_intelligence is not None