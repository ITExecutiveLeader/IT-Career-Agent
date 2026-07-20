from crewai import Task

from app.agents.agents import (
    resume_analyst,
    job_analyst,
    career_strategist,
    interview_coach,
    ats_match_agent
)


def create_resume_review_task(resume_text: str) -> Task:
    """Create the resume analysis task."""

    return Task(
        description=f"""
            Analyze this candidate resume:

            --------------------
            {resume_text}
            --------------------

            Identify:

            - Technical skills
            - Experience level
            - Strengths
            - Weaknesses
            - Missing qualifications
            - Recommended improvements
            """,

            expected_output=(
            "A detailed resume analysis using the provided resume "
            "and relevant ATS and recruiting knowledge."
            ),
            agent=resume_analyst
        )


def create_job_analysis_task(job_text: str) -> Task:
    """Create the job analysis task."""

    return Task(
        description=f"""
            Analyze this job description:

            --------------------
            {job_text}
            --------------------

            Identify:

            - Required skills
            - Technologies
            - Certifications
            - Experience expectations
            - ATS keywords
            """,
        expected_output=(
            "A structured breakdown of job requirements."
        ),
        agent=job_analyst
    )


def create_career_strategy_task(context: list[Task]) -> Task:
    """Create the career strategy task."""

    return Task(
        description=(
            "Using the resume analysis and job analysis, "
            "create a career strategy that improves the "
            "candidate's chances of getting hired."
        ),

        expected_output=(
            "A practical action plan covering skills, "
            "resume changes, certifications, "
            "and job search strategy."
        ),

        agent=career_strategist,
        context=context
    )


def create_interview_prep_task(context: list[Task]) -> Task:
    """Create the interview preparation task."""

    return Task(
        description=(
            "Create an interview preparation plan "
            "based on the candidate profile "
            "and target role."
        ),

        expected_output=(
            "A list of technical questions, "
            "behavioral questions, "
            "and preparation recommendations."
        ),

        agent=interview_coach,
        context=context
    )


def create_ats_match_task(resume_task: Task, job_task: Task) -> Task:
    """Create the ATS compatibility analysis task."""

    return Task(
        description="""
            Compare the Resume Analysis with the Job Analysis.

            Generate:

            • ATS Match Score
            • Matching Skills
            • Missing Skills
            • Missing Keywords
            • Strongest Qualifications
            • Weakest Areas
            • Resume Improvements
            """,

            expected_output="A complete ATS compatibility report.",

            agent=ats_match_agent,

            context=[
                resume_task,
                job_task
            ]
        )


def create_career_tasks(resume_text: str, job_text: str) -> list[Task]:
    """
    Create all CrewAI tasks for the career analysis workflow.
    """

    tasks: dict[str, Task] = {}

    tasks["resume"] = create_resume_review_task(resume_text)

    tasks["job"] = create_job_analysis_task(job_text)

    tasks["career"] = create_career_strategy_task( 
        context=[
            tasks["resume"],
            tasks["job"]
        ]
    )

    tasks["interview"] = create_interview_prep_task(
        context=[
            tasks["resume"],
            tasks["job"],
            tasks["career"]
        ]
    )

    tasks["ats"] = create_ats_match_task(
        tasks["resume"],
        tasks["job"]
    )

    return [
    tasks["resume"],
    tasks["job"],
    tasks["career"],
    tasks["interview"],
    tasks["ats"],
]
