from app.models import ATSResult, JobData, ResumeData

from .analyzer import Analyzer


class SkillAnalyzer(Analyzer):
    """
    Compares resume skills against job requirements.
    """

    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:

        resume_skills = {
            skill.lower()
            for skill in resume.skills
        }

        required_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        matched = sorted(
            resume_skills & required_skills
        )

        missing = sorted(
            required_skills - resume_skills
        )

        result.matched_skills = matched

        result.missing_skills = missing