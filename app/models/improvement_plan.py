from dataclasses import dataclass, field


@dataclass
class ImprovementPlan:
    """
    Structured recommendations for improving a resume.
    """

    executive_assessment: str = ""

    high_priority_items: list[str] = field(default_factory=list)

    quick_wins: list[str] = field(default_factory=list)

    long_term_improvements: list[str] = field(default_factory=list)

    sections_to_improve: list[str] = field(default_factory=list)