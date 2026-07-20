from app.models import CareerContext
from app.models import CareerIntelligence


class CareerIntelligenceService:
    """
    Converts ATS results into a reusable intelligence model.
    """

    def build(
        self,
        context: CareerContext,
    ) -> CareerIntelligence:

        ats = context.ats_result

        if ats is None:
            raise ValueError("ATS analysis results are required")

        return CareerIntelligence(

            overall_score=ats.overall_score,

            executive_summary=ats.executive_summary,

            matched_skills=ats.matched_skills,

            missing_skills=ats.missing_skills,

            priority_gaps=ats.priority_gaps,

            category_scores=ats.category_scores,

            recommendations=ats.recommendations,
        )