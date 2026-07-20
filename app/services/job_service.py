from app.models import CareerContext
from app.parsers.job_parser import JobParser
from app.services.file_loader import FileLoader


class JobService:
    """
    Coordinates loading and parsing a job description.
    """

    def __init__(self):

        self.loader = FileLoader()

        self.parser = JobParser()

    def load_job(
        self,
        file_path: str,
    ) -> CareerContext:

        text = self.loader.load(file_path)

        job = self.parser.parse(text)

        return CareerContext(
            job_description=job
        )