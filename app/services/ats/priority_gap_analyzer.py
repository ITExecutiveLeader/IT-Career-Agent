from app.models import ATSResult, JobData, ResumeData

from .analyzer import Analyzer
from .skill_weights import SKILL_WEIGHTS


class PriorityGapAnalyzer(Analyzer):
    """
    Orders missing skills by business importance.
    """

    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:

        result.priority_gaps = sorted(
            result.missing_skills,
            key=lambda skill: (
                SKILL_WEIGHTS.get(
                    skill.lower(),
                    1,
                ),
                skill,
            ),
            reverse=True,
        )