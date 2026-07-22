from app.models import CareerContext

from app.services.resume_service import ResumeService
from app.services.job_service import JobService
from app.services.ats.ats_service import ATSService
from app.services.career_intelligence_service import CareerIntelligenceService
from app.services.improvement_planner import ImprovementPlannerService


class AnalysisService:
    """
    Coordinates the complete career analysis workflow.
    """

    def __init__(self):

        self.resume_service = ResumeService()

        self.job_service = JobService()

        self.ats_service = ATSService()

        self.career_intelligence_service = CareerIntelligenceService()

        self.improvement_planner = ImprovementPlannerService()

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

        if context.resume is None:
            raise ValueError("Resume data was not loaded successfully")
        
        context.job_description = (
            job_context.job_description
        )

        if context.job_description is None:
            raise ValueError("Job data was not loaded successfully")

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

        context.improvement_plan = (
            self.improvement_planner.create_plan(
                resume_score=int(context.ats_result.overall_score),
                missing_skills=context.ats_result.missing_skills,
                weak_sections=context.ats_result.priority_gaps,
            )
        )

        return context
    
    def analyze_bytes(
        self,
        resume_bytes: bytes,
        job_bytes: bytes,
    ) -> CareerContext:

        context = CareerContext()

        resume_context = (
            self.resume_service.load_resume_bytes(
                resume_bytes
            )
        )

        job_context = (
            self.job_service.load_job_bytes(
                job_bytes
            )
        )

        context.resume = resume_context.resume

        if context.resume is None:
            raise ValueError(
                "Resume data was not loaded successfully"
            )

        context.job_description = (
            job_context.job_description
        )

        if context.job_description is None:
            raise ValueError(
                "Job data was not loaded successfully"
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

        context.improvement_plan = (
            self.improvement_planner.create_plan(
                resume_score=int(
                    context.ats_result.overall_score
                ),
                missing_skills=context.ats_result.missing_skills,
                weak_sections=context.ats_result.priority_gaps,
            )
        )

        return context