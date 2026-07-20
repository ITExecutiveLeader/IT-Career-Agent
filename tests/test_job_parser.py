from app.parsers.job_parser import JobParser


def test_job_parser_returns_job_data():

    parser = JobParser()

    text = """
            Looking for a Python developer
            with AWS and Terraform.
            """

    job = parser.parse(text)

    assert job.raw_text == text

    assert "python" in job.required_skills
    assert "aws" in job.required_skills
    assert "terraform" in job.required_skills

    assert job.responsibilities == []