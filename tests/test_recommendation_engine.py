from app.models import ATSResult
from app.recommendations import RecommendationEngine


def test_recommendation_engine():

    result = ATSResult()

    result.missing_skills = [
        "vendor management",
        "itil",
        "pmp",
    ]

    engine = RecommendationEngine()

    recommendations = engine.build(result)

    assert len(recommendations) == 3

    assert recommendations[0].title == "Add vendor management"

    assert recommendations[0].priority == "High"

    assert recommendations[0].category == "Skill Gap"

    assert recommendations[0].resume_section == (
        "Professional Experience"
    )

    assert (
        "ATS"
        in recommendations[0].expected_impact
    )