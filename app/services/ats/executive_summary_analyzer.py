from app.models import ATSResult, JobData, ResumeData

from .analyzer import Analyzer


class ExecutiveSummaryAnalyzer(Analyzer):
    """
    Produces an executive-level summary of ATS results.
    """

    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:

        summary = []

        #
        # Overall assessment
        #

        score = result.overall_score

        if score >= 90:
            summary.append(
                "The candidate is an exceptional match for this position."
            )

        elif score >= 80:
            summary.append(
                "The candidate is a strong match for this position."
            )

        elif score >= 65:
            summary.append(
                "The candidate is a good match with several areas for improvement."
            )

        else:
            summary.append(
                "The candidate has significant skill gaps for this position."
            )

        #
        # Strongest categories
        #

        strong_categories = [
            category
            for category, value
            in result.category_scores.items()
            if value >= 80
        ]

        if strong_categories:

            summary.append(
                "Key strengths include "
                + ", ".join(strong_categories)
                + "."
            )

        #
        # Highest priority gaps
        #

        if result.priority_gaps:

            summary.append(
                "Highest priority improvement areas include "
                + ", ".join(result.priority_gaps[:3])
                + "."
            )

        #
        # Recommendation
        #

        if score >= 80:

            summary.append(
                "Overall recommendation: Strong candidate for further consideration."
            )

        elif score >= 65:

            summary.append(
                "Overall recommendation: Candidate should be considered after addressing key gaps."
            )

        else:

            summary.append(
                "Overall recommendation: Candidate requires significant development before being competitive."
            )

        result.executive_summary = " ".join(summary)