import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import the prompt and tool function from within the same package
from .prompts import AUDIT_LOG_AGENT_PROMPT
from .tools import query_gcp_audit_logs

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create a FunctionTool from the query_gcp_audit_logs function
# The ADK will automatically infer the schema for this tool from the function's type hints and docstring.
query_audit_logs_tool = FunctionTool(
    func=query_gcp_audit_logs,
)

# Define the BQ Audit Log Agent
# Using "gemini-1.5-pro-001" as planned. Ensure this model is available in your Vertex AI project and location.
audit_log_agent = Agent(
    model=GEMINI_MODEL_NAME,
    name="audit_log_agent",
    description="A specialized agent that constructs and executes BigQuery SQL queries to retrieve GCP audit logs based on user requests. It uses the query_gcp_audit_logs tool.",
    instruction=AUDIT_LOG_AGENT_PROMPT,
    tools=[query_audit_logs_tool]
)

if __name__ == '__main__':
    # This section is for basic testing or direct invocation of the agent if needed.
    # For a full interactive experience, you'll typically run this via the ADK CLI or Web UI,
    # especially when it's part of a larger multi-agent system.

    print(f"BQ Audit Log Agent (audit_log_agent) has been initialized with model: {GEMINI_MODEL_NAME}.")
    print(f"System Prompt:\n{AUDIT_LOG_AGENT_PROMPT[:500]}... (truncated)") # Print a snippet
    print(f"Tools available: {[tool.name for tool in audit_log_agent.tools]}")

    # Example of how you might test the agent's response to a prompt (requires ADK setup to run):
    # try:
    #     response = audit_log_agent.send("Show me the last 5 admin actions related to GCS buckets.")
    #     print(f"\nAgent Response:\n{response.text}")
    #     if response.tool_calls:
    #         print(f"\nTool Calls Made:")
    #         for tc in response.tool_calls:
    #             print(f"  - Tool: {tc.tool_name}, Args: {tc.args}")
    # except Exception as e:
    #     print(f"Error during agent send: {e}")
    print("\nTo test interactively, use 'adk web' or 'adk talk' once the root agent is set up.") 