from autogen_agentchat.agents import AssistantAgent
from literature_review_GPT.Models import ollama_model_client
from prompts import research_prompt,summary_prompt
from tools import Arvix_tool

def summarizer_agent(model_client):

    return AssistantAgent(
                name = "summarizer_agent",
                model_client=model_client,
                description="Produces a short Markdown review from provided papers.",
                system_message=summary_prompt.Summarizer_assistant_prompt,
                
                )