import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=600

)

research_agent = Agent(
    role="Research Analyst",
    goal="Find information about the topic",
    backstory="Expert researcher who collects reliable information",
    llm=llm,
    verbose=True
)

summary_agent = Agent(
    role="Summarization Expert",
    goal="Summarize research information",
    backstory="Expert at summarizing long research content",
    llm=llm,
    verbose=True
)

fact_checker_agent = Agent(
    role="Fact Checker",
    goal="Verify correctness of research information",
    backstory="Responsible for checking facts and accuracy",
    llm=llm,
    verbose=True
)

report_agent = Agent(
    role="Report Writer",
    goal="Generate a structured research report",
    backstory="Professional writer who prepares detailed reports",
    llm=llm,
    verbose=True
)
