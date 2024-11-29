# utils.py
# This module provides utility functions and classes used across the agent system.
# It includes task context management, OpenAI API integration, and prompt generation.

import os
from typing import Dict, Any
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI client with API key from environment
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class TaskContext:
    """Stores context and parameters for agent tasks"""
    def __init__(self, task_type: str, parameters: Dict[str, Any]):
        # Initialize task context with type and parameters
        self.task_type = task_type
        self.parameters = parameters
        self.results = None

    def update_results(self, results: Any):
        """
        Update task results with new data
        Args:
            results: New results to store
        """
        self.results = results

    def get_context_summary(self) -> str:
        """
        Get a summary of the task context
        Returns:
            str: Formatted summary of task type, parameters, and results
        """
        return f"Task Type: {self.task_type}\nParameters: {self.parameters}\nResults: {self.results}"

def create_agent_prompt(agent_type: str, parameters: Dict[str, Any]) -> str:
    """
    Create a prompt for agent initialization based on type and parameters
    
    Args:
        agent_type: Type of agent (research, writing, analysis)
        parameters: Configuration parameters for the agent
        
    Returns:
        str: Generated prompt for the agent
    """
    # Start with a base prompt identifying the agent type
    base_prompt = f"You are a specialized {agent_type} agent. "
    
    # Add specific instructions based on agent type
    if agent_type == "research":
        return base_prompt + f"Your task is to research about {parameters.get('topic', 'the given topic')} " \
                           f"and provide comprehensive information."
    elif agent_type == "writing":
        return base_prompt + f"Your task is to write content in a {parameters.get('style', 'general')} style " \
                           f"based on the provided information."
    elif agent_type == "analysis":
        return base_prompt + f"Your task is to analyze the provided data and extract meaningful insights."
    
    return base_prompt + "Your specific tasks will be provided in the execution context."

def get_agent_response(prompt: str) -> str:
    """
    Get response from OpenAI API for agent tasks
    
    Args:
        prompt: The prompt to send to the OpenAI API
        
    Returns:
        str: Generated response from the API
    """
    try:
        # Make API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Execute the assigned task."}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting agent response: {e}")
        return f"Error: {str(e)}"
