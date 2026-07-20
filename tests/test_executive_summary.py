from app.models import ATSResult
from app.parsers.resume_parser import ResumeParser
from app.parsers.job_parser import JobParser

from app.services.ats.skill_analyzer import SkillAnalyzer
from app.services.ats.category_analyzer import CategoryAnalyzer
from app.services.ats.priority_gap_analyzer import PriorityGapAnalyzer
from app.services.ats.score_calculator import ScoreCalculator
from app.services.ats.executive_summary_analyzer import (
    ExecutiveSummaryAnalyzer,
)


def test_executive_summary():

    resume = ResumeParser().parse(
        """
        AWS
        Azure
        CISSP
        Incident Response
        SQL
        IT Strategy
        Vendor Management
        """
    )

    job = JobParser().parse(
        """
        AWS
        Azure
        Terraform
        CISSP
        Incident Response
        SQL
        IT Strategy
        Vendor Management
        """
    )

    result = ATSResult()

    SkillAnalyzer().analyze(
        resume,
        job,
        result,
    )

    CategoryAnalyzer().analyze(
        resume,
        job,
        result,
    )

    PriorityGapAnalyzer().analyze(
        resume,
        job,
        result,
    )

    ScoreCalculator().calculate(
        result,
    )

    ExecutiveSummaryAnalyzer().analyze(
        resume,
        job,
        result,
    )

    assert len(result.executive_summary) > 50

    assert (
        "candidate"
        in result.executive_summary.lower()
    )