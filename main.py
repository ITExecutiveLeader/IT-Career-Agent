from app.agents.crew_builder import build_career_crew
from tools import load_document


def main():

    resume_text = load_document(
        "resumes/sample_resume.txt"
    )

    job_text = load_document(
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