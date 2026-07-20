from app.services.file_loader import FileLoader
from app.parsers.resume_parser import ResumeParser


def test_resume_extracts_executive_it_skills():

    loader = FileLoader()

    parser = ResumeParser()

    text = loader.load(
        "tests/data/sample_resume.pdf"
    )

    resume = parser.parse(text)

    expected_skills = [
        "aws",
        "azure",
        "cissp",
        "enterprise architecture",
        "incident response",
        "it strategy",
        "power bi",
        "sql",
        "vendor management",
    ]

    for skill in expected_skills:
        assert skill in resume.skills