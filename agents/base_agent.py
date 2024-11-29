# base_agent.py
# This module defines the base agent class that all specialized agents inherit from.
# It provides common functionality and interface that all agents must implement.

from abc import ABC, abstractmethod
from typing import Any, Optional
from utils import TaskContext, get_agent_response, create_agent_prompt

class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, context: TaskContext):
        # Initialize the agent with its task context
        self.context = context
        # Create the initial prompt for the agent based on its type and parameters
        self.prompt = create_agent_prompt(context.task_type, context.parameters)
        
    @abstractmethod
    def execute_task(self, input_data: Optional[Any] = None) -> Any:
        """
        Execute the agent's primary task
        Must be implemented by all derived agent classes
        """
        pass
    
    def get_response(self, additional_prompt: str = "") -> str:
        """
        Get a response from the agent using the OpenAI API
        Args:
            additional_prompt: Extra context or instructions for this specific request
        """
        full_prompt = f"{self.prompt}\n{additional_prompt}"
        return get_agent_response(full_prompt)
    
    def update_context(self, new_data: Any):
        """
        Update the agent's context with new data
        Useful for maintaining state between multiple task executions
        """
        self.context.update_results(new_data)
        
    def get_status(self) -> str:
        """
        Get the current status of the agent
        Returns a summary of the agent's context and task results
        """
        return self.context.get_context_summary()
