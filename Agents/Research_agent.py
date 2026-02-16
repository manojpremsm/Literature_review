from autogen_agentchat.agents import AssistantAgent
from literature_review_GPT.Models import ollama_model_client
from prompts import research_prompt,summary_prompt
from tools import Arvix_tool

def Research_agent1(model_client):

    reserach_assistant = AssistantAgent(
                name = "reserach_agent",
                model_client=model_client,
                description="Crafts arXiv queries and retrieves candidate papers.",
                system_message=research_prompt.Research_assistant_promt,
                tools=[Arvix_tool.arvix_tool()],
                reflect_on_tool_use=True

                )
    
    return reserach_assistant