from dataclasses import dataclass


@dataclass(slots=True)
class Recommendation:
    """
    Represents one actionable recommendation for improving
    the resume.
    """

    title: str
    description: str
    priority: str
    category: str
    resume_section: str
    expected_impact: str