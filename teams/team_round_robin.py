from autogen_agentchat.teams import RoundRobinGroupChat
from Agents import Research_agent,Summarizer_agent

def team_creation(model_client):

    
    team= RoundRobinGroupChat(
                                [Research_agent.Research_agent1(model_client),Summarizer_agent.summarizer_agent(model_client)],
                                max_turns=2  
                                    )
    return team