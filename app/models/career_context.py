from __future__ import annotations

from dataclasses import dataclass, field

from .ats_result import ATSResult
from .job import JobData
from .resume import ResumeData
from .career_intelligence import CareerIntelligence


@dataclass
class CareerContext:
    """
    Shared application state used throughout the career workflow.
    """

    resume: ResumeData | None = None

    job_description: JobData | None = None

    ats_result: ATSResult | None = None

    metadata: dict[str, str] = field(
        default_factory=dict
    )

    warnings: list[str] = field(
        default_factory=list
    )

    career_intelligence: CareerIntelligence | None = None