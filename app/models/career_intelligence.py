from dataclasses import dataclass, field


@dataclass
class CareerIntelligence:
    """
    Consolidated career analysis produced by the ATS engine.
    """

    overall_score: float = 0.0

    executive_summary: str = ""

    matched_skills: list[str] = field(
        default_factory=list
    )

    missing_skills: list[str] = field(
        default_factory=list
    )

    priority_gaps: list[str] = field(
        default_factory=list
    )

    category_scores: dict[str, float] = field(
        default_factory=dict
    )

    recommendations: list[str] = field(
        default_factory=list
    )