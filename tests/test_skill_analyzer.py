from app.models import ATSResult, JobData, ResumeData
from app.services.ats.skill_analyzer import SkillAnalyzer


def test_skill_analyzer():

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
            "docker",
            "terraform",
        ]
    )

    result = ATSResult()

    analyzer = SkillAnalyzer()

    analyzer.analyze(
        resume,
        job,
        result,
    )

    assert result.matched_skills == [
        "docker",
        "python",
    ]

    assert result.missing_skills == [
        "terraform",
    ]