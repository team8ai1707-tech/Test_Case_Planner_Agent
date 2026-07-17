# agent.py
from .fetch_github_file import fetch_github_file
from google.adk.agents.llm_agent import Agent

qa_instruction = """... (your instructions here) ..."""

root_agent = Agent(
    model='gemini-2.5-flash',
    name='test_plan_agent',
    description='A QA agent that reads code from GitHub and generates detailed test plans.',
    instruction=qa_instruction,
    tools=[fetch_github_file] 
)