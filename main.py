import asyncio
from typing import List,Dict,AsyncGenerator
from autogen_agentchat.messages import (TextMessage)
from autogen_agentchat.ui import Console
from teams import team_round_robin
from Models import ollama_model_client

async def run_litrev(
        
        topic: str,
        num_papers: int = 5,
        
    ) -> AsyncGenerator[str, None]:
        """Yield strings representing the conversation in real‑time."""
       
        team = team_round_robin.team_creation(ollama_model_client.ollama_model_client())
        print(team)
        try:
             
            task_prompt = (
                f"Conduct a literature review on **{topic}** and return exactly {num_papers} papers."
            )

            async for msg in team.run_stream(task=task_prompt):
               
                if isinstance(msg, TextMessage):
                    yield f"{msg.source}: {msg.content}"
            await team.reset() 
        except Exception as e:
             print(e)
             