import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import the prompt and tool functions from within the same package
from .prompts import COMPUTE_MONITORING_LOG_AGENT_PROMPT
from .tools import list_compute_monitoring_log_tables, query_gcp_compute_monitoring_logs

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create FunctionTools for the compute monitoring agent
list_tables_tool = FunctionTool(
    func=list_compute_monitoring_log_tables,
)

query_compute_monitoring_logs_tool = FunctionTool(
    func=query_gcp_compute_monitoring_logs,
)

# Define the Compute Monitoring Log Agent
compute_monitoring_log_agent = Agent(
    model=GEMINI_MODEL_NAME,
    name="compute_monitoring_log_agent",
    description="A specialized agent for GCP compute monitoring logs. It can list available compute monitoring log tables in BigQuery and execute SQL queries against them using the list_compute_monitoring_log_tables and query_gcp_compute_monitoring_logs tools respectively.",
    instruction=COMPUTE_MONITORING_LOG_AGENT_PROMPT,
    tools=[
        list_tables_tool,
        query_compute_monitoring_logs_tool
    ]
)

if __name__ == '__main__':
    print(f"Compute Monitoring Log Agent (compute_monitoring_log_agent) has been initialized with model: {GEMINI_MODEL_NAME}.")
    print(f"System Prompt:\n{COMPUTE_MONITORING_LOG_AGENT_PROMPT[:500]}... (truncated)")
    print(f"Tools available: {[tool.name for tool in compute_monitoring_log_agent.tools]}")
    print("\nTo test interactively, use 'adk web' or 'adk talk' once the root agent is set up.") 