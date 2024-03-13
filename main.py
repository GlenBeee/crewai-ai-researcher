import sys
from crewai import Agent, Task
import os
from dotenv import load_dotenv
from crewai import Crew, Process
#from langchain_openai import AzureChatOpenAI

load_dotenv()

from langchain_openai import ChatOpenAI
default_llm = ChatOpenAI(
    model="mistral", # ollama
    openai_api_base="http://localhost:11434/v1", # ollama
    #openai_api_base="http://localhost:1234/v1", # LM Studio
    api_key="NotUsed"
)

# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  llm=default_llm,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  agent=researcher  # Assigning the task to the researcher
)


# Instantiate your crew
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()