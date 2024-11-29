# API Reference

## Agent Manager

### Class: `AgentManager`

#### Methods

##### `create_agent(agent_type: str, parameters: Dict[str, Any]) -> BaseAgent`
Creates a new agent of the specified type.

Parameters:
- `agent_type`: Type of agent to create ("research", "writing", "analysis")
- `parameters`: Configuration parameters for the agent

Returns:
- Instance of the created agent

Example:
```python
manager = AgentManager()
agent = manager.create_agent("research", {"topic": "AI advances"})
```

##### `execute_agent_task(agent_id: str, input_data: Any = None) -> Any`
Executes a task with the specified agent.

Parameters:
- `agent_id`: ID of the agent to execute the task
- `input_data`: Optional input data for the task

Returns:
- Result of the task execution

##### `get_agent(agent_id: str) -> BaseAgent`
Retrieves an agent by its ID.

##### `list_agents() -> List[str]`
Returns a list of all active agent IDs.

##### `remove_agent(agent_id: str)`
Removes an agent from the system.

## Agent Factory

### Class: `AgentFactory`

#### Methods

##### `create_agent(agent_type: str, parameters: Dict[str, Any]) -> BaseAgent`
Creates a new agent based on the specified type and parameters.

##### `get_available_agent_types() -> List[str]`
Returns list of available agent types.

## Base Agent

### Class: `BaseAgent`

#### Methods

##### `execute_task(input_data: Optional[Any] = None) -> Any`
Abstract method that must be implemented by all agent classes.

##### `get_response(additional_prompt: str = "") -> str`
Gets a response from the OpenAI API.

##### `update_context(new_data: Any)`
Updates the agent's context with new data.

##### `get_status() -> str`
Returns the current status of the agent.

## Specialized Agents

### Class: `ResearchAgent`

#### Methods

##### `execute_task(input_data: Optional[Any] = None) -> Any`
Executes research task based on the given topic.

### Class: `WritingAgent`

#### Methods

##### `execute_task(input_data: Optional[Any] = None) -> Any`
Generates written content in the specified style.

### Class: `AnalysisAgent`

#### Methods

##### `execute_task(input_data: Optional[Any] = None) -> Any`
Analyzes provided data and generates insights.
