from crewai import Crew, Process

from app.agents.agents import (
    resume_analyst,
    job_analyst,
    career_strategist,
    interview_coach,
    ats_match_agent
)

from app.agents.tasks import create_career_tasks


def build_career_crew(
    resume_text: str,
    job_text: str
) -> Crew:
    """
    Build the Career AI Crew using the supplied
    resume and job description.
    """

    tasks = create_career_tasks(
        resume_text,
        job_text
    )

    return Crew(
        agents=[
            resume_analyst,
            job_analyst,
            career_strategist,
            interview_coach,
            ats_match_agent
        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True
    )