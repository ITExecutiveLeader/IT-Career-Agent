from app.models import ATSResult, JobData, ResumeData

from .analyzer import Analyzer


class RecommendationAnalyzer(Analyzer):
    """
    Generates recommendations based on ATS analysis.
    """

    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:

        recommendations = []

        for skill in result.priority_gaps:
            recommendations.append(
                f"Add {skill} experience if applicable."
            )

        result.recommendations = recommendations