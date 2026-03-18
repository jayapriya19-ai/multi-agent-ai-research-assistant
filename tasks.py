from crewai import Task
from agents import research_agent, summary_agent, fact_checker_agent, report_agent
research_task = Task(
    description="Research the topic: {topic} and collect important information",
    agent=research_agent,
    expected_output="Detailed research information about the topic"
)

summary_task = Task(
    description="Create a complete structured research report about {topic} including introduction, types, characteristics, applications, advantages, and conclusion. The response must be complete and not cut off.",
    agent=summary_agent,
    expected_output="Full structured research report"
)

fact_task = Task(
    description="Fact check the research about {topic}",
    agent=fact_checker_agent,
    expected_output="Verified research information"
)

report_task = Task(
    description="Create a structured report about {topic}",
    agent=report_agent,
    expected_output="Final report with introduction, body and conclusion"
)