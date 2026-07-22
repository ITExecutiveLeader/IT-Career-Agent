from pathlib import Path

from fastapi.testclient import TestClient

from app.api.main import app


client = TestClient(app)


def test_analyze_endpoint_returns_career_report():

    resume_path = Path(
        "tests/data/sample_resume.pdf"
    )

    job_path = Path(
        "tests/data/sample_job.pdf"
    )

    with (
        resume_path.open("rb") as resume_file,
        job_path.open("rb") as job_file,
    ):

        response = client.post(
            "/analyze",
            files={
                "resume_file": (
                    "sample_resume.pdf",
                    resume_file,
                    "application/pdf",
                ),
                "job_file": (
                    "sample_job.pdf",
                    job_file,
                    "application/pdf",
                ),
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["title"]
    assert data["content"]

    assert data["ats_score"] is not None

    assert "matched_skills" in data

    assert "missing_skills" in data

    assert "recommendations" in data

    assert "improvement_plan" in data