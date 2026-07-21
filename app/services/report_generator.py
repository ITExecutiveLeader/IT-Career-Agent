from app.models import CareerContext, CareerReport


class ReportGenerator:
    """
    Generates user-facing career reports.
    """

    def generate(
        self,
        context: CareerContext,
    ) -> CareerReport:

        if context.ats_result is None:
            raise ValueError(
                "Cannot generate report without ATS results."
            )

        ats = context.ats_result
        intelligence = context.career_intelligence

        sections = []

        sections.append(
            "# IT Career Analysis Report"
        )

        if intelligence:
            sections.append(
                f"""
## Executive Summary

{intelligence.executive_summary or "No summary available."}
"""
            )

            sections.append(
                f"""
## Overall Match Score

{intelligence.overall_score:.1f}%
"""
            )

        sections.append(
            f"""
## Strengths

{self._format_list(ats.strengths)}
"""
        )

        sections.append(
            f"""
## Matched Skills

{self._format_list(ats.matched_skills)}
"""
        )

        sections.append(
            f"""
## Missing Skills

{self._format_list(ats.missing_skills)}
"""
        )

        sections.append(
            f"""
## Priority Gaps

{self._format_list(ats.priority_gaps)}
"""
        )

        sections.append(
            f"""
## Recommendations

{self._format_list(ats.recommendations)}
"""
        )

        if ats.notes:
            sections.append(
                f"""
## Notes

{ats.notes}
"""
            )

        if context.improvement_plan:

            plan_items = []

            for item in context.improvement_plan.items:
                plan_items.append(
                    f"""
### Priority {item.priority}: {item.category}

**Issue:**  
{item.issue}

**Recommendation:**  
{item.recommendation}

**Impact:**  
{item.impact}
"""
                )

            sections.append(
                """
## Improvement Plan

"""
                + "\n".join(plan_items)
            )

        content = "\n".join(sections)

        return CareerReport(
            title="IT Career Analysis Report",
            content=content.strip(),
        )

    @staticmethod
    def _format_list(
        items: list[str],
    ) -> str:

        if not items:
            return "- None"

        return "\n".join(
            f"- {item}"
            for item in items
        )