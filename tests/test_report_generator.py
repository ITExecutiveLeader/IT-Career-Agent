from app.models import ATSResult, CareerContext
from app.services.report_generator import ReportGenerator


def test_report_generator():

    context = CareerContext(
        ats_result=ATSResult(
            matched_skills=[
                "python",
                "aws",
            ],
            missing_skills=[
                "terraform",
            ],
            recommendations=[
                "Add Terraform experience if applicable."
            ],
        )
    )

    generator = ReportGenerator()

    report = generator.generate(
        context
    )

    assert report.title == (
        "IT Career Analysis Report"
    )

    assert "python" in report.content

    assert "terraform" in report.content

    assert (
        "Add Terraform experience"
        in report.content
    )