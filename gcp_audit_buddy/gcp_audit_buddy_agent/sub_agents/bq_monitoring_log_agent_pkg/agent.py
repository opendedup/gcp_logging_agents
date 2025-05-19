import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import the prompt and tool functions from within the same package
from .prompts import MONITORING_LOG_AGENT_PROMPT
from .tools import list_monitoring_log_tables, query_gcp_monitoring_logs

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create FunctionTools for the monitoring agent
list_tables_tool = FunctionTool(
    func=list_monitoring_log_tables,
)

query_monitoring_logs_tool = FunctionTool(
    func=query_gcp_monitoring_logs,
)

# Define the BQ Monitoring Log Agent
monitoring_log_agent = Agent(
    model=GEMINI_MODEL_NAME,
    name="monitoring_log_agent",
    description="A specialized agent for GCP monitoring logs. It can list available monitoring log tables in BigQuery and execute SQL queries against them using the list_monitoring_log_tables and query_gcp_monitoring_logs tools respectively.",
    instruction=MONITORING_LOG_AGENT_PROMPT,
    tools=[
        list_tables_tool,
        query_monitoring_logs_tool
    ]
)

if __name__ == '__main__':
    print(f"BQ Monitoring Log Agent (monitoring_log_agent) has been initialized with model: {GEMINI_MODEL_NAME}.")
    print(f"System Prompt:\n{MONITORING_LOG_AGENT_PROMPT[:500]}... (truncated)")
    print(f"Tools available: {[tool.name for tool in monitoring_log_agent.tools]}")
    print("\nTo test interactively, use 'adk web' or 'adk talk' once the root agent is set up.") 