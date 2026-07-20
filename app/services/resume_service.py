from app.models import CareerContext
from app.parsers.resume_parser import ResumeParser
from app.services.file_loader import FileLoader


class ResumeService:
    """
    Coordinates loading and parsing a resume.
    """

    def __init__(self):

        self.loader = FileLoader()

        self.parser = ResumeParser()

    def load_resume(
        self,
        file_path: str,
    ) -> CareerContext:

        text = self.loader.load(file_path)

        resume = self.parser.parse(text)

        return CareerContext(
            resume=resume
        )