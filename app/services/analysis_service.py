from app.models import CareerContext

from app.services.resume_service import ResumeService
from app.services.job_service import JobService
from app.services.ats.ats_service import ATSService
from app.services.career_intelligence_service import CareerIntelligenceService


class AnalysisService:
    """
    Coordinates the complete career analysis workflow.
    """

    def __init__(self):

        self.resume_service = ResumeService()

        self.job_service = JobService()

        self.ats_service = ATSService()

        self.career_intelligence_service = CareerIntelligenceService()

    def analyze(
        self,
        resume_path: str,
        job_path: str,
    ) -> CareerContext:

        context = CareerContext()

        resume_context = (
            self.resume_service.load_resume(
                resume_path
            )
        )

        job_context = (
            self.job_service.load_job(
                job_path
            )
        )

        context.resume = resume_context.resume

        context.job_description = (
            job_context.job_description
        )

        context.ats_result = (
            self.ats_service.analyze(
                context.resume,
                context.job_description,
            )
        )

        context.career_intelligence = (
            self.career_intelligence_service.build(
                context
            )
        )      

        return context