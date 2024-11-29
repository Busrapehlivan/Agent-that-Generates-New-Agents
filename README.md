# Dynamic Agent Generator System

A sophisticated multi-agent framework capable of autonomously creating and managing specialized AI agents for complex tasks. This system leverages OpenAI's GPT models to create intelligent agents that can perform research, writing, and analysis tasks.

## Features

- **Multiple Agent Types:**
  - Research Agent: Gathers information on specific topics
  - Writing Agent: Creates content in various styles
  - Analysis Agent: Provides insights and analysis
  
- **Flexible Architecture:**
  - Factory pattern for dynamic agent creation
  - Modular design for easy extension
  - Context preservation between agent interactions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Busrapehlivan/Agent-that-Generates-New-Agents.git
cd Agent-that-Generates-New-Agents
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

The system can be used by running the `main.py` file, which demonstrates the basic workflow:

```python
from agent_manager import AgentManager

# Create agent manager
manager = AgentManager()

# Create a research agent
research_agent = manager.create_agent("research", {
    "topic": "Latest developments in artificial intelligence"
})

# Execute research task
research_results = research_agent.execute_task()

# Create a writing agent to transform research into content
writing_agent = manager.create_agent("writing", {
    "style": "technical blog post"
})

# Generate content based on research
blog_post = writing_agent.execute_task(research_results)
```

## Project Structure

```
.
├── agent_factory.py      # Factory for creating specialized agents
├── agent_manager.py      # Main manager for coordinating agents
├── agents/
│   ├── __init__.py
│   ├── analysis_agent.py # Specialized analysis agent
│   ├── base_agent.py     # Abstract base class for all agents
│   ├── research_agent.py # Specialized research agent
│   └── writing_agent.py  # Specialized writing agent
├── main.py              # Example usage and demonstration
├── requirements.txt     # Project dependencies
└── utils.py            # Utility functions and OpenAI integration
```

## Dependencies

- Python 3.8+
- OpenAI API (GPT-4)
- Required Python packages:
  - openai==1.3.5
  - python-dotenv==1.0.0

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Büşra Pehlivan

## Acknowledgments

- OpenAI for providing the GPT API
- The Python community for excellent libraries and tools
