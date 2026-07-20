from app.parsers.resume_parser import ResumeParser


def test_resume_parser_returns_resume_data():

    parser = ResumeParser()

    text = """
            John Doe
            Python Developer

            Skills:
            Python
            AWS
            Docker
            Git
            """

    resume = parser.parse(text)

    assert resume.raw_text == text

    assert "python" in resume.skills
    assert "aws" in resume.skills
    assert "docker" in resume.skills

    assert resume.projects == []