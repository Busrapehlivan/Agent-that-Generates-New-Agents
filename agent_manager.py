# agent_manager.py
# This module implements the main agent manager that coordinates all agent activities.
# It handles agent creation, tracking, and task execution.

from typing import Dict, Any, List
from agent_factory import AgentFactory
from agents.base_agent import BaseAgent

class AgentManager:
    """Main class for managing the creation and interaction of agents"""
    
    def __init__(self):
        # Initialize collections to store active agents
        self.agents: Dict[str, BaseAgent] = {}
        # Create an agent factory instance
        self.agent_factory = AgentFactory()
        
    def create_agent(self, agent_type: str, parameters: Dict[str, Any]) -> BaseAgent:
        """
        Create a new agent of the specified type
        
        Args:
            agent_type: Type of agent to create
            parameters: Configuration parameters for the agent
            
        Returns:
            BaseAgent: The created agent instance
        """
        # Create a new agent using the factory
        agent = self.agent_factory.create_agent(agent_type, parameters)
        # Generate a unique ID for the agent
        agent_id = f"{agent_type}_{len(self.agents)}"
        # Store the agent in our collection
        self.agents[agent_id] = agent
        return agent
    
    def get_agent(self, agent_id: str) -> BaseAgent:
        """
        Get an agent by its ID
        
        Args:
            agent_id: Unique identifier of the agent
            
        Returns:
            BaseAgent: The requested agent instance
        """
        return self.agents.get(agent_id)
    
    def list_agents(self) -> List[str]:
        """
        Get a list of all active agent IDs
        
        Returns:
            List[str]: List of agent IDs
        """
        return list(self.agents.keys())
    
    def remove_agent(self, agent_id: str):
        """
        Remove an agent from the system
        
        Args:
            agent_id: ID of the agent to remove
        """
        if agent_id in self.agents:
            del self.agents[agent_id]
            
    def get_available_agent_types(self) -> List[str]:
        """
        Get a list of available agent types
        
        Returns:
            List[str]: List of supported agent types
        """
        return self.agent_factory.get_available_agent_types()
    
    def execute_agent_task(self, agent_id: str, input_data: Any = None) -> Any:
        """
        Execute a task with the specified agent
        
        Args:
            agent_id: ID of the agent to execute the task
            input_data: Optional input data for the task
            
        Returns:
            Any: Result of the task execution
            
        Raises:
            ValueError: If the specified agent is not found
        """
        agent = self.get_agent(agent_id)
        if agent:
            return agent.execute_task(input_data)
        raise ValueError(f"Agent not found: {agent_id}")
    
    def get_agent_status(self, agent_id: str) -> str:
        """
        Get the current status of an agent
        
        Args:
            agent_id: ID of the agent to check
            
        Returns:
            str: Current status of the agent
            
        Raises:
            ValueError: If the specified agent is not found
        """
        agent = self.get_agent(agent_id)
        if agent:
            return agent.get_status()
        raise ValueError(f"Agent not found: {agent_id}")
