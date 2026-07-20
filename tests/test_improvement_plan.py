from app.models.improvement_plan import (
    ImprovementItem,
    ImprovementPlan,
)


def test_improvement_item_creation():

    item = ImprovementItem(
        priority=1,
        category="Professional Summary",
        issue="Missing cloud leadership keywords",
        recommendation="Add Azure and AWS architecture experience",
        impact="High",
    )

    assert item.priority == 1
    assert item.category == "Professional Summary"
    assert item.impact == "High"


def test_improvement_plan_creation():

    item = ImprovementItem(
        priority=1,
        category="Experience",
        issue="Weak achievement statements",
        recommendation="Add measurable outcomes",
        impact="Medium",
    )

    plan = ImprovementPlan(
        overall_score=75,
        items=[item],
    )

    assert plan.overall_score == 75
    assert len(plan.items) == 1