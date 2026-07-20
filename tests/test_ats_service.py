from app.models import JobData, ResumeData
from app.services.ats.ats_service import ATSService


def test_ats_service():

    resume = ResumeData(
        skills=[
            "python",
            "aws",
            "docker",
        ]
    )

    job = JobData(
        required_skills=[
            "python",
            "terraform",
            "docker",
        ]
    )

    service = ATSService()

    result = service.analyze(
        resume,
        job,
    )

    assert result.matched_skills == [
        "docker",
        "python",
    ]

    assert result.missing_skills == [
        "terraform",
    ]

    assert len(result.recommendations) == 1

    assert result.overall_score == 62.5