"""
Pydantic request and response models.
"""

from pydantic import BaseModel, Field


class ImprovementItemResponse(BaseModel):
    """
    Improvement recommendation returned by the API.
    """

    priority: int

    category: str

    issue: str

    recommendation: str

    impact: str


class AnalyzeResponse(BaseModel):
    """
    Response returned from career analysis.
    """

    title: str

    content: str

    format: str

    ats_score: float | None = None

    executive_summary: str | None = None

    matched_skills: list[str] = Field(
        default_factory=list
    )

    missing_skills: list[str] = Field(
        default_factory=list
    )

    recommendations: list[str] = Field(
        default_factory=list
    )

    improvement_plan: list[ImprovementItemResponse] = Field(
        default_factory=list
    )