from abc import ABC, abstractmethod

from app.models import ATSResult, JobData, ResumeData


class BaseAnalyzer(ABC):
    """
    Base class for all ATS analyzers.
    """

    @abstractmethod
    def analyze(
        self,
        resume: ResumeData,
        job: JobData,
        result: ATSResult,
    ) -> None:
        """
        Update the ATSResult in place.
        """
        raise NotImplementedError