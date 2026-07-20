"""
Pydantic request and response models.
"""

from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    """
    Response returned from career analysis.
    """

    title: str

    content: str

    format: str

    ats_score: float | None = None

    matched_skills: list[str] = []

    missing_skills: list[str] = []

    recommendations: list[str] = []