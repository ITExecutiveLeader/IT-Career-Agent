from app.models import ATSResult, JobData, ResumeData
from app.services.ats.recommendation_analyzer import RecommendationAnalyzer


def test_recommendation_analyzer():

    resume = ResumeData()

    job = JobData()

    result = ATSResult(
    missing_skills=[
        "terraform",
        "kubernetes",
    ],
    priority_gaps=[
        "terraform",
        "kubernetes",
    ],
    )

    analyzer = RecommendationAnalyzer()

    analyzer.analyze(
        resume,
        job,
        result,
    )

    assert len(result.recommendations) == 2

    assert "terraform" in result.recommendations[0].lower()