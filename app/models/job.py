from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class JobData:
    """
    Structured representation of a job description.
    """

    title: str | None = None

    company: str | None = None

    location: str | None = None

    summary: str | None = None

    responsibilities: list[str] = field(default_factory=list)

    required_skills: list[str] = field(default_factory=list)

    preferred_skills: list[str] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    education: list[str] = field(default_factory=list)

    raw_text: str = ""