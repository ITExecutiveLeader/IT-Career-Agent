from app.models import ATSResult
from app.parsers.job_parser import JobParser
from app.parsers.resume_parser import ResumeParser
from app.services.ats.category_analyzer import CategoryAnalyzer


def test_category_scores():

    resume = ResumeParser().parse(
        """
        AWS
        Azure
        CISSP
        Incident Response
        SQL
        Power BI
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
        """
    )

    result = ATSResult()

    CategoryAnalyzer().analyze(
        resume,
        job,
        result,
    )

    assert result.category_scores["Cloud"] == 66.67

    assert result.category_scores["Cybersecurity"] == 100.0

    assert result.category_scores["Data"] == 100.0