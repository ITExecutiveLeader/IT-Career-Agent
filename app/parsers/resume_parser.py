from app.models import ResumeData
from app.parsers.certification_extractor import extract_certifications
from app.parsers.skill_extractor import extract_skills


class ResumeParser:
    """
    Parses resume text into a structured ResumeData model.

    Initial implementation stores the raw text only.
    Future versions will extract structured fields.
    """

    def parse(
        self,
        text: str,
    ) -> ResumeData:

        return ResumeData(
            raw_text=text,
            skills=extract_skills(text),
            certifications=extract_certifications(text),
        )