from app.models import ATSResult
from app.models import CareerContext
from app.services.career_intelligence_service import (
    CareerIntelligenceService,
)


def test_build_career_intelligence():

    ats = ATSResult()

    ats.overall_score = 88

    ats.executive_summary = "Excellent fit."

    ats.matched_skills = ["aws"]

    ats.priority_gaps = ["terraform"]

    ats.recommendations = [
        "Add Terraform experience."
    ]

    context = CareerContext()

    context.ats_result = ats

    intelligence = (
        CareerIntelligenceService().build(
            context
        )
    )

    assert intelligence.overall_score == 88

    assert intelligence.executive_summary == (
        "Excellent fit."
    )

    assert intelligence.priority_gaps == [
        "terraform"
    ]