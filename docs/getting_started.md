# Getting Started

This guide will help you set up and start using the Dynamic Agent Generator System.

## Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- An OpenAI API key
- Git installed (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Busrapehlivan/Agent-that-Generates-New-Agents.git
cd Agent-that-Generates-New-Agents
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Quick Start

Here's a simple example to get you started:

```python
from agent_manager import AgentManager

# Initialize the agent manager
manager = AgentManager()

# Create a research agent
research_agent = manager.create_agent("research", {
    "topic": "Latest developments in artificial intelligence"
})

# Execute research task
research_results = research_agent.execute_task()
print("Research Results:", research_results)

# Create a writing agent
writing_agent = manager.create_agent("writing", {
    "style": "technical blog post"
})

# Generate content based on research
blog_post = writing_agent.execute_task(research_results)
print("Generated Blog Post:", blog_post)
```

## Common Use Cases

### 1. Research and Content Generation
```python
# Research a topic and create content
research_agent = manager.create_agent("research", {"topic": "quantum computing"})
research_data = research_agent.execute_task()

writing_agent = manager.create_agent("writing", {"style": "educational"})
article = writing_agent.execute_task(research_data)
```

### 2. Content Analysis
```python
# Analyze existing content
analysis_agent = manager.create_agent("analysis", {
    "focus": "content quality"
})
analysis = analysis_agent.execute_task(article)
```

### 3. Multi-Agent Workflow
```python
# Chain multiple agents together
research_data = research_agent.execute_task()
draft = writing_agent.execute_task(research_data)
analysis = analysis_agent.execute_task(draft)
final_content = writing_agent.execute_task(analysis)
```

## Best Practices

1. **Error Handling**
```python
try:
    result = agent.execute_task(input_data)
except Exception as e:
    print(f"Error executing task: {e}")
```

2. **Resource Management**
```python
# Clean up agents when done
manager.remove_agent(agent_id)
```

3. **Context Management**
```python
# Update agent context with new data
agent.update_context(new_data)
```

## Troubleshooting

Common issues and solutions:

1. **API Key Issues**
   - Ensure `.env` file exists and contains valid API key
   - Check environment variable is properly loaded

2. **Import Errors**
   - Verify all dependencies are installed
   - Check Python version compatibility

3. **Execution Errors**
   - Validate input data format
   - Check agent type is supported
   - Ensure sufficient API credits

## Next Steps

- Explore the [API Reference](api_reference.md) for detailed documentation
- Review the [Architecture Guide](architecture.md) for system design details
- Check the example scripts in `main.py`
