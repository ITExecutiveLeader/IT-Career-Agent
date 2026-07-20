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