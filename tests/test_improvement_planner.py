from app.services.improvement_planner import (
    ImprovementPlannerService,
)


def test_improvement_planner_creates_plan():

    service = ImprovementPlannerService()

    plan = service.create_plan(
        resume_score=72,
        weak_sections=[
            "Professional Summary",
            "Experience",
        ],
        missing_skills=[
            "Kubernetes",
            "Terraform",
        ],
    )

    assert plan.overall_score == 72
    assert len(plan.items) == 3

    assert plan.items[0].category == "Professional Summary"
    assert plan.items[1].category == "Experience"
    assert plan.items[2].category == "Skills"


def test_improvement_planner_handles_empty_input():

    service = ImprovementPlannerService()

    plan = service.create_plan(
        resume_score=90
    )

    assert plan.overall_score == 90
    assert len(plan.items) == 0