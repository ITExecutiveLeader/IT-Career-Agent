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

        content = f"""
# IT Career Analysis Report

## Matched Skills

{self._format_list(ats.matched_skills)}

## Missing Skills

{self._format_list(ats.missing_skills)}

## Recommendations

{self._format_list(ats.recommendations)}
"""

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