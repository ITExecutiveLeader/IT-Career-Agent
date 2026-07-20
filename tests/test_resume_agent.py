from app.agents.agents import resume_analyst
from crewai import Task, Crew, Process


def test_resume_agent_with_rag():

    task = Task(
        description="""
        Analyze this resume:

        John Smith
        Systems Administrator

        Skills:
        Windows Server
        Active Directory
        PowerShell
        Azure
        VMware

        Provide:
        - Strengths
        - Weaknesses
        - ATS recommendations

        Use the knowledge base when helpful.
        """,
        expected_output="""
        A structured resume analysis with ATS recommendations.
        """,
        agent=resume_analyst
    )


    crew = Crew(
        agents=[
            resume_analyst
        ],
        tasks=[
            task
        ],
        process=Process.sequential,
        verbose=True
    )


    result = crew.kickoff()

    print("\nAGENT RESULT:\n")
    print(result)

    assert result
