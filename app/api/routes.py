"""
API routes.
"""

import tempfile
from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)
from sqlalchemy.orm import Session

from app.api.schemas import AnalyzeResponse
from app.database.dependencies import get_db
from app.database.repository import (
    create_analysis,
    create_resume,
    get_or_create_user,
)
from app.services.analysis_service import AnalysisService
from app.services.report_generator import ReportGenerator


router = APIRouter()

analysis_service = AnalysisService()
report_generator = ReportGenerator()


@router.get("/health")
def health_check():
    """
    Health endpoint.
    """

    return {
        "status": "ok",
        "service": "IT Career Agent",
    }


@router.post(
    "/analyze",
    response_model=AnalyzeResponse,
)
async def analyze(
    resume_file: UploadFile = File(...),
    job_file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Analyze a resume against a job description.
    """

    if resume_file.filename is None:
        raise ValueError(
            "Resume file name is missing"
        )

    if job_file.filename is None:
        raise ValueError(
            "Job file name is missing"
        )

    user = get_or_create_user(
        db,
        email="default@career-agent.local",
        display_name="Default User",
    )

    with tempfile.TemporaryDirectory() as temp_dir:

        resume_path = Path(temp_dir) / resume_file.filename
        job_path = Path(temp_dir) / job_file.filename

        resume_bytes = await resume_file.read()
        resume_path.write_bytes(resume_bytes)

        job_bytes = await job_file.read()
        job_path.write_bytes(job_bytes)

        resume_text = resume_path.read_text(
            errors="ignore"
        )

        resume_record = create_resume(
            db,
            user_id=user.id,
            filename=resume_file.filename,
            raw_text=resume_text,
        )

        context = analysis_service.analyze(
            str(resume_path),
            str(job_path),
        )

        report = report_generator.generate(
            context
        )

        ats_score = None
        matched_skills = None
        missing_skills = None
        recommendations = None

        if context.ats_result is not None:
            ats_score = float(
                context.ats_result.overall_score
            )

        if context.career_intelligence is not None:
            matched_skills = ", ".join(
                context.career_intelligence.matched_skills
            )

            missing_skills = ", ".join(
                context.career_intelligence.missing_skills
            )

            recommendations = ", ".join(
                context.career_intelligence.recommendations
            )

        create_analysis(
            db,
            user_id=user.id,
            resume_id=resume_record.id,
            job_description=job_path.read_text(
                errors="ignore"
            ),
            report_content=report.content,
            ats_score=ats_score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            recommendations=recommendations,
        )

        return AnalyzeResponse(
            title=report.title,
            content=report.content,
            format=report.format,
        )