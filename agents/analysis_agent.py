# analysis_agent.py
# This module implements a specialized agent for analyzing content and providing insights.
# It can process various types of input data and generate analytical reports.

from typing import Any, Optional
from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    """Agent specialized in analysis tasks"""
    
    def execute_task(self, input_data: Optional[Any] = None) -> Any:
        """
        Execute analysis task on the provided data
        
        Args:
            input_data: The content or data to be analyzed
            
        Returns:
            str: Analysis results and insights about the provided data
        """
        # Construct the base analysis prompt
        prompt = "Analyze the following data and provide insights"
        
        # Add the data to be analyzed if provided
        if input_data:
            prompt += f"\nData to analyze:\n{input_data}"
        else:
            # Handle the case where no data is provided
            prompt += "\nNo data provided for analysis"
            
        # Get the analysis results using the OpenAI API
        analysis_results = self.get_response(prompt)
        
        # Update the agent's context with the analysis results
        self.update_context(analysis_results)
        
        return analysis_results
