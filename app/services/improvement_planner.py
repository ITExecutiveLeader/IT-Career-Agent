from app.models import (
    ATSResult,
    ImprovementPlan,
)


class ImprovementPlanner:
    """
    Builds a deterministic resume improvement plan.
    """

    def build(
        self,
        ats_result: ATSResult,
    ) -> ImprovementPlan:

        plan = ImprovementPlan()

        # Executive assessment
        if ats_result.overall_score >= 85:
            plan.executive_assessment = (
                "Excellent alignment with the target role."
            )

        elif ats_result.overall_score >= 70:
            plan.executive_assessment = (
                "Strong alignment with several opportunities for improvement."
            )

        else:
            plan.executive_assessment = (
                "Significant improvements recommended before applying."
            )

        # High priority = missing skills
        plan.high_priority_items = list(
            ats_result.missing_skills
        )

        # Quick wins
        plan.quick_wins = list(
            ats_result.missing_skills[:3]
        )

        # Resume sections
        plan.sections_to_improve = [
            "Professional Summary",
            "Skills",
        ]

        if ats_result.missing_skills:
            plan.sections_to_improve.append(
                "Professional Experience"
            )

        # Long-term improvements
        for skill in ats_result.missing_skills:

            if skill in {
                "pmp",
                "itil",
                "cissp",
            }:

                plan.long_term_improvements.append(
                    skill.upper()
                )

        return plan