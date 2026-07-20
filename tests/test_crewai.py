from crewai import Agent

agent = Agent(
    role="Tester",
    goal="Verify CrewAI works.",
    backstory="Simple test agent.",
    verbose=True
)

print("✅ CrewAI is working!")