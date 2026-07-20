from app.models import ATSResult
from app.parsers.job_parser import JobParser
from app.parsers.resume_parser import ResumeParser
from app.services.ats.priority_gap_analyzer import (
    PriorityGapAnalyzer,
)


def test_priority_gap_order():

    resume = ResumeParser().parse(
        """
        AWS
        CISSP
        """
    )

    job = JobParser().parse(
        """
        AWS
        CISSP
        Vendor Management
        Python
        IT Strategy
        """
    )

    result = ATSResult()

    result.missing_skills = [
        "vendor management",
        "python",
        "it strategy",
    ]

    PriorityGapAnalyzer().analyze(
        resume,
        job,
        result,
    )

    assert result.priority_gaps == [
        "vendor management",
        "it strategy",
        "python",
    ]