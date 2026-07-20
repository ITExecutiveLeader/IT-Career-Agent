from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResumeData:
    """
    Structured representation of a candidate's resume.
    """

    name: str | None = None

    email: str | None = None

    phone: str | None = None

    location: str | None = None

    summary: str | None = None

    skills: list[str] = field(default_factory=list)

    experience: list[str] = field(default_factory=list)

    education: list[str] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)

    raw_text: str = ""