from app.models import ATSResult, JobData, ResumeData

from .analyzer import Analyzer
from .skill_categories import SKILL_CATEGORIES


class CategoryAnalyzer(Analyzer):
    """
    Calculates ATS match percentage for each skill category.
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

        job_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        scores = {}

        for category, category_skills in SKILL_CATEGORIES.items():

            required = job_skills & category_skills

            if not required:
                continue

            matched = resume_skills & required

            score = (
                len(matched)
                /
                len(required)
            ) * 100

            scores[category] = round(
                score,
                2,
            )

        result.category_scores = scores