from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ATSResult:
    """
    Results of comparing a resume with a job description.
    """

    overall_score: float = 0.0

    matched_skills: list[str] = field(default_factory=list)

    missing_skills: list[str] = field(default_factory=list)

    matched_certifications: list[str] = field(default_factory=list)

    missing_certifications: list[str] = field(default_factory=list)

    matched_education: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    notes: str = ""

    category_scores: dict[str, float] = field(default_factory=dict)

    strengths: list[str] = field(default_factory=list)

    priority_gaps: list[str] = field(default_factory=list)

    executive_summary: str = ""