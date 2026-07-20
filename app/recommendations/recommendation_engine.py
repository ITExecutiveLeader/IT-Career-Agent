from app.models import ATSResult

from .recommendation import Recommendation


class RecommendationEngine:
    """
    Converts ATS findings into structured recommendations.
    """

    def build(
        self,
        ats_result: ATSResult,
    ) -> list[Recommendation]:

        recommendations = []

        for skill in ats_result.missing_skills:

            recommendations.append(
                Recommendation(
                    title=f"Add {skill}",
                    description=(
                        f"Demonstrate measurable experience with "
                        f"{skill} in your resume."
                    ),
                    priority="High",
                    category="Skill Gap",
                    resume_section="Professional Experience",
                    expected_impact=(
                        "Increase ATS match score."
                    ),
                )
            )

        return recommendations