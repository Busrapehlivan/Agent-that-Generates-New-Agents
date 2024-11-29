# agent_factory.py
# This module implements the Factory pattern for creating different types of AI agents.
# It provides a centralized way to instantiate specialized agents based on task requirements.

from typing import Dict, Any, Optional
from agents.base_agent import BaseAgent
from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent
from agents.analysis_agent import AnalysisAgent
from utils import TaskContext

class AgentFactory:
    """Factory class for creating specialized agents"""
    
    @staticmethod
    def create_agent(agent_type: str, parameters: Dict[str, Any]) -> Optional[BaseAgent]:
        """
        Create a new agent based on the specified type and parameters
        
        Args:
            agent_type: Type of agent to create (research, writing, analysis)
            parameters: Configuration parameters for the agent
            
        Returns:
            BaseAgent: An instance of the specified agent type
        """
        # Create a task context with the provided parameters
        context = TaskContext(agent_type, parameters)
        
        # Return the appropriate agent type based on the request
        if agent_type == "research":
            return ResearchAgent(context)
        elif agent_type == "writing":
            return WritingAgent(context)
        elif agent_type == "analysis":
            return AnalysisAgent(context)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
            
    @staticmethod
    def get_available_agent_types() -> list:
        """Get a list of available agent types"""
        return ["research", "writing", "analysis"]
