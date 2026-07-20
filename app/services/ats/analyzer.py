from abc import ABC, abstractmethod

from app.models import ATSResult, JobData, ResumeData


class Analyzer(ABC):
    """
    Base class for ATS analyzers.
    """

    @abstractmethod
    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:
        """
        Update the ATS result in place.
        """
        ...