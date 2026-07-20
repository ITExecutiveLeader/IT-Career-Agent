from app.agents.crew_builder import build_career_crew
from app.services.file_loader import FileLoader


def main():

    loader = FileLoader()

    resume_text = loader.load(
        "resumes/sample_resume.txt"
    )

    job_text = loader.load(
        "job_descriptions/sample_job.txt"
    )

    crew = build_career_crew(
        resume_text,
        job_text
    )

    result = crew.kickoff()

    print("\n===== CAREER REPORT =====\n")

    print(result)


if __name__ == "__main__":
    main()