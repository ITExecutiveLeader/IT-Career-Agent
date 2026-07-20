from app.models import ATSResult
from app.services.improvement_planner import (
    ImprovementPlanner,
)


def test_improvement_planner():

    result = ATSResult()

    result.overall_score = 72

    result.missing_skills = [
        "vendor management",
        "itil",
        "pmp",
    ]

    planner = ImprovementPlanner()

    plan = planner.build(result)

    assert plan.executive_assessment.startswith(
        "Strong"
    )

    assert "vendor management" in plan.high_priority_items

    assert "Professional Summary" in plan.sections_to_improve

    assert "ITIL" in plan.long_term_improvements

    assert "PMP" in plan.long_term_improvements