from dataclasses import dataclass


@dataclass
class CareerReport:
    """
    User-facing career analysis report.
    """

    title: str

    content: str

    format: str = "markdown"