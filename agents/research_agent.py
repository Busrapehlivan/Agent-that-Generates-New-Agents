# research_agent.py
# This module implements a specialized agent for conducting research tasks.
# It can gather information on specific topics and provide detailed findings.

from typing import Any, Optional
from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    """Agent specialized in research tasks"""
    
    def execute_task(self, input_data: Optional[Any] = None) -> Any:
        """
        Execute research task based on the given topic
        
        Args:
            input_data: Optional additional context or parameters for the research
            
        Returns:
            str: Research findings and information about the specified topic
        """
        # Get the research topic from the agent's parameters
        topic = self.context.parameters.get('topic', 'general topic')
        
        # Construct the research prompt
        prompt = f"Research the following topic and provide detailed information: {topic}"
        
        # Add any additional context if provided
        if input_data:
            prompt += f"\nAdditional context: {input_data}"
            
        # Get the research results using the OpenAI API
        research_results = self.get_response(prompt)
        
        # Update the agent's context with the findings
        self.update_context(research_results)
        
        return research_results
