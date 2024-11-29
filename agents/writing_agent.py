# writing_agent.py
# This module implements a specialized agent for writing and content creation tasks.
# It can generate various types of content in different styles based on input data.

from typing import Any, Optional
from .base_agent import BaseAgent

class WritingAgent(BaseAgent):
    """Agent specialized in writing tasks"""
    
    def execute_task(self, input_data: Optional[Any] = None) -> Any:
        """
        Execute writing task based on the given style and input data
        
        Args:
            input_data: Optional content or information to base the writing on
            
        Returns:
            str: Generated written content in the specified style
        """
        # Get the writing style from the agent's parameters
        style = self.context.parameters.get('style', 'general')
        
        # Construct the base writing prompt
        prompt = f"Write content in a {style} style"
        
        # Include any provided input data as context for the writing
        if input_data:
            prompt += f"\nBased on the following information:\n{input_data}"
        
        # Generate the content using the OpenAI API
        written_content = self.get_response(prompt)
        
        # Update the agent's context with the generated content
        self.update_context(written_content)
        
        return written_content
