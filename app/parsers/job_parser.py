from app.models import JobData
from app.parsers.skill_extractor import extract_skills
from .certification_extractor import extract_certifications


class JobParser:
    """
    Parses job description text into a structured JobData model.

    Initial implementation stores the raw text only.
    """

    def parse(
        self,
        text: str,
    ) -> JobData:

        return JobData(
            raw_text=text,
            required_skills=extract_skills(text),
            certifications=extract_certifications(text),
        )