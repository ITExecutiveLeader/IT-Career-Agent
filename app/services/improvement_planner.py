from app.models.improvement_plan import (
    ImprovementItem,
    ImprovementPlan,
)


class ImprovementPlannerService:
    """
    Generates prioritized resume improvement recommendations.
    """

    def create_plan(
        self,
        resume_score: int,
        missing_skills: list[str] | None = None,
        weak_sections: list[str] | None = None,
    ) -> ImprovementPlan:

        items: list[ImprovementItem] = []

        priority = 1

        if weak_sections:
            for section in weak_sections:
                items.append(
                    ImprovementItem(
                        priority=priority,
                        category=section,
                        issue=f"{section} needs improvement",
                        recommendation=(
                            f"Strengthen {section} using "
                            "achievement-based statements "
                            "with measurable outcomes"
                        ),
                        impact="High",
                    )
                )

                priority += 1

        if missing_skills:
            items.append(
                ImprovementItem(
                    priority=priority,
                    category="Skills",
                    issue="Missing relevant skills",
                    recommendation=(
                        "Add missing technical skills "
                        "aligned with target positions"
                    ),
                    impact="Medium",
                )
            )

        return ImprovementPlan(
            overall_score=resume_score,
            items=items,
        )