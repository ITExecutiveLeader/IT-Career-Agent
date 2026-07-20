from app.models import ATSResult, JobData, ResumeData

from .recommendation_analyzer import RecommendationAnalyzer
from .score_calculator import ScoreCalculator
from .skill_analyzer import SkillAnalyzer
from .category_analyzer import CategoryAnalyzer
from .priority_gap_analyzer import PriorityGapAnalyzer
from .executive_summary_analyzer import ExecutiveSummaryAnalyzer


class ATSService:
    """
    Coordinates execution of ATS analyzers.
    """

    def __init__(self):

        self.analyzers = [
            SkillAnalyzer(),
            CategoryAnalyzer(),
            PriorityGapAnalyzer(),
            RecommendationAnalyzer(),
        ]

        self.score_calculator = ScoreCalculator()

    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
    ) -> ATSResult:

        result = ATSResult()

        for analyzer in self.analyzers:
            analyzer.analyze(
            resume,
            job,
            result,
        )

        self.score_calculator.calculate(
            result
        )

        ExecutiveSummaryAnalyzer().analyze(
            resume,
            job,
            result,
        )

        return result