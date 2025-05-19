import os
from dotenv import load_dotenv
from google_adk.agents import Agent
from google_adk.tools import FunctionTool

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
    name="list_monitoring_log_tables",
    description="Lists all available tables in the configured GCP monitoring logs BigQuery dataset."
)

query_monitoring_logs_tool = FunctionTool(
    func=query_gcp_monitoring_logs,
    name="query_gcp_monitoring_logs",
    description="Executes a BigQuery SQL query to retrieve GCP monitoring logs and returns the results as a JSON string."
)

# Define the BQ Monitoring Log Agent
monitoring_log_agent = Agent(
    model=GEMINI_MODEL_NAME,
    system_prompt=MONITORING_LOG_AGENT_PROMPT,
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