"""
API routes.
"""

import tempfile
from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.api.schemas import AnalyzeResponse
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
):
    """
    Analyze a resume against a job description.
    """

    with tempfile.TemporaryDirectory() as temp_dir:

        resume_path = Path(temp_dir) / resume_file.filename

        job_path = Path(temp_dir) / job_file.filename


        resume_path.write_bytes(
            await resume_file.read()
        )

        job_path.write_bytes(
            await job_file.read()
        )


        context = analysis_service.analyze(
            str(resume_path),
            str(job_path),
        )


        report = report_generator.generate(
            context
        )


        return AnalyzeResponse(
            title=report.title,
            content=report.content,
            format=report.format,
        )