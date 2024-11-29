# Examples

This document provides practical examples of using the Dynamic Agent Generator System in various scenarios.

## Basic Examples

### 1. Simple Research Task

```python
from agent_manager import AgentManager

manager = AgentManager()

# Create and execute a research task
research_agent = manager.create_agent("research", {
    "topic": "Artificial Intelligence in Healthcare"
})
findings = research_agent.execute_task()
print(findings)
```

### 2. Content Generation

```python
# Create a writing agent for blog posts
writing_agent = manager.create_agent("writing", {
    "style": "technical blog",
    "tone": "professional"
})

# Generate a blog post
blog_post = writing_agent.execute_task("AI technologies in modern healthcare")
print(blog_post)
```

### 3. Content Analysis

```python
# Analyze content quality
analysis_agent = manager.create_agent("analysis", {
    "focus": "content quality",
    "metrics": ["readability", "engagement", "accuracy"]
})

analysis_result = analysis_agent.execute_task(blog_post)
print(analysis_result)
```

## Advanced Examples

### 1. Multi-Agent Workflow

```python
# Research -> Write -> Analyze -> Refine workflow
def create_refined_content(topic: str):
    # Initialize manager
    manager = AgentManager()
    
    # Create agents
    research_agent = manager.create_agent("research", {"topic": topic})
    writing_agent = manager.create_agent("writing", {"style": "blog"})
    analysis_agent = manager.create_agent("analysis", {"focus": "quality"})
    
    # Execute workflow
    research_data = research_agent.execute_task()
    initial_draft = writing_agent.execute_task(research_data)
    analysis = analysis_agent.execute_task(initial_draft)
    final_content = writing_agent.execute_task(analysis)
    
    return final_content

# Use the workflow
content = create_refined_content("Latest AI Trends 2024")
```

### 2. Parallel Processing

```python
import asyncio
from typing import List

async def parallel_research(topics: List[str]):
    manager = AgentManager()
    agents = []
    results = []
    
    # Create agents for each topic
    for topic in topics:
        agent = manager.create_agent("research", {"topic": topic})
        agents.append(agent)
    
    # Execute tasks in parallel
    async def execute_task(agent):
        return await agent.execute_task()
    
    tasks = [execute_task(agent) for agent in agents]
    results = await asyncio.gather(*tasks)
    
    return results

# Use parallel processing
topics = ["AI in Healthcare", "AI in Finance", "AI in Education"]
results = asyncio.run(parallel_research(topics))
```

### 3. Custom Agent Configuration

```python
# Create a specialized research agent with custom parameters
research_agent = manager.create_agent("research", {
    "topic": "Quantum Computing",
    "depth": "technical",
    "sources": ["academic", "industry"],
    "time_range": "last_year",
    "language": "technical"
})

# Execute with additional context
context = {
    "focus_areas": ["algorithms", "hardware"],
    "exclude_topics": ["quantum cryptography"],
    "required_citations": True
}

results = research_agent.execute_task(context)
```

### 4. Error Handling and Retry Logic

```python
from typing import Optional
import time

def execute_with_retry(agent, max_retries: int = 3, delay: int = 2):
    retries = 0
    last_error: Optional[Exception] = None
    
    while retries < max_retries:
        try:
            return agent.execute_task()
        except Exception as e:
            last_error = e
            retries += 1
            if retries < max_retries:
                time.sleep(delay)
            
    raise Exception(f"Failed after {max_retries} retries. Last error: {last_error}")

# Use retry logic
try:
    agent = manager.create_agent("research", {"topic": "Complex topic"})
    result = execute_with_retry(agent)
except Exception as e:
    print(f"Task failed: {e}")
```

### 5. Context-Aware Processing

```python
def process_with_context(topic: str, previous_research: str = None):
    manager = AgentManager()
    
    # Create research agent with context
    research_agent = manager.create_agent("research", {
        "topic": topic,
        "context": previous_research
    })
    
    # Update context based on new findings
    new_findings = research_agent.execute_task()
    research_agent.update_context(new_findings)
    
    # Create writing agent with accumulated context
    writing_agent = manager.create_agent("writing", {
        "style": "academic",
        "previous_content": previous_research
    })
    
    # Generate content using all available context
    return writing_agent.execute_task(new_findings)

# Use context-aware processing
initial_research = process_with_context("AI Basics")
advanced_research = process_with_context("AI Advanced Topics", initial_research)
```
