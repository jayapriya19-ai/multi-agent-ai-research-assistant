import streamlit as st
import time
from crewai import Crew
from agents import research_agent, summary_agent
from tasks import research_task, summary_task

st.title("Multi-Agent AI Research Assistant")

topic = st.text_input("Enter research topic")

if st.button("Generate Report"):

    if topic == "":
        st.warning("Please enter a research topic.")

    else:
        crew = Crew(
            agents=[
                research_agent,
                summary_agent
            ],
            tasks=[
                research_task,
                summary_task
            ]
        )

        try:
            time.sleep(3)
            result = crew.kickoff(inputs={"topic": topic})
            st.write(result.raw)

        except Exception:
            st.error("Rate limit reached. Please wait 30 seconds and try again.")