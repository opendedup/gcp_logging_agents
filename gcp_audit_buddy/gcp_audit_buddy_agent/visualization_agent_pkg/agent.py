import os
from dotenv import load_dotenv
from google_adk.agents import Agent
from google_adk.tools import FunctionTool

# Import the prompt and tool function from within the same package
from .prompts import VISUALIZATION_AGENT_PROMPT
from .tools import create_report_visualization

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create a FunctionTool from the create_report_visualization function
visualization_tool = FunctionTool(
    func=create_report_visualization,
    name="create_report_visualization", 
    description="Generates a data visualization (SVG or PNG) from a JSON string and returns it as an image Part."
)

# Define the Visualization Agent
visualization_agent = Agent(
    model=GEMINI_MODEL_NAME,
    system_prompt=VISUALIZATION_AGENT_PROMPT,
    tools=[visualization_tool],
    # The visualization agent's output (the Part object from the tool)
    # should be returned directly without further LLM processing.
    # We achieve this by instructing the LLM in the prompt to *only* return the tool output.
    # If more complex behavior were needed (e.g., deciding if a chart is even possible
    # before calling the tool), this agent might be more conversational.
)

if __name__ == '__main__':
    print(f"Visualization Agent (visualization_agent) has been initialized with model: {GEMINI_MODEL_NAME}.")
    print(f"System Prompt:\n{VISUALIZATION_AGENT_PROMPT[:500]}... (truncated)")
    print(f"Tools available: {[tool.name for tool in visualization_agent.tools]}")
    print("\nTo test interactively, use 'adk web' or 'adk talk' once the root agent is set up and calls this agent.") 