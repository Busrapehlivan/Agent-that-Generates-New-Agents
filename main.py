# main.py
# This is the main entry point of the agent system.
# It demonstrates how to create and use different types of agents together.

from agent_manager import AgentManager

def main():
    # Create the main agent manager that will coordinate all agents
    manager = AgentManager()
    
    # Example 1: Create a research agent to gather information about AI
    print("\nCreating Research Agent...")
    research_agent = manager.create_agent("research", {
        "topic": "Latest developments in artificial intelligence"
    })
    
    # Execute research task and get results
    print("\nExecuting Research Task...")
    research_results = research_agent.execute_task()
    print("\nResearch Results:")
    print(research_results)
    
    # Example 2: Create a writing agent to transform research into a blog post
    print("\nCreating Writing Agent...")
    writing_agent = manager.create_agent("writing", {
        "style": "technical blog post"
    })
    
    # Use the research results to create a blog post
    print("\nGenerating Blog Post...")
    blog_post = writing_agent.execute_task(research_results)
    print("\nBlog Post:")
    print(blog_post)
    
    # Example 3: Create an analysis agent to evaluate the blog post
    print("\nCreating Analysis Agent...")
    analysis_agent = manager.create_agent("analysis", {
        "focus": "content quality and engagement potential"
    })
    
    # Analyze the blog post content
    print("\nAnalyzing Content...")
    analysis = analysis_agent.execute_task(blog_post)
    print("\nContent Analysis:")
    print(analysis)
    
    # Display information about all active agents
    print("\nActive Agents:")
    for agent_id in manager.list_agents():
        print(f"Agent ID: {agent_id}")
        print(manager.get_agent_status(agent_id))
        print()

if __name__ == "__main__":
    main()
