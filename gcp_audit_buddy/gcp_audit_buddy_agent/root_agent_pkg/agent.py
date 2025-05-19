import os
from dotenv import load_dotenv
from google_adk.agents import Agent
from google_adk.tools import FunctionTool, AgentTool

# Import the root agent's prompt and its direct tools
from .prompts import ROOT_AGENT_PROMPT
from .tools import call_mcp_time_service

# Import the specialist sub-agents
# These paths are relative to the current gcp_audit_buddy_agent package
from ..bq_audit_log_agent_pkg.agent import audit_log_agent
from ..bq_monitoring_log_agent_pkg.agent import monitoring_log_agent
from ..visualization_agent_pkg.agent import visualization_agent

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create a FunctionTool for the MCP Time Service
mcp_time_tool = FunctionTool(
    func=call_mcp_time_service,
    name="get_gmt_time_offset", # Name used in the ROOT_AGENT_PROMPT
    description="Calls the external MCP Time Service to get current GMT or GMT with an offset. Input: offset_hours (int, optional). Output: {\"gmt_time\": \"YYYY-MM-DDTHH:MM:SSZ\", \"offset_applied_hours\": offset_hours}."
)

# Create AgentTools for the specialist sub-agents
# The names here MUST match the names used in the ROOT_AGENT_PROMPT
audit_log_investigator_tool = AgentTool(
    agent=audit_log_agent,
    name="gcp_audit_log_investigator",
    description="Delegates tasks to the BQ Audit Log Agent, an expert in querying GCP Audit Logs (Admin Activity, Data Access) in BigQuery."
)

monitoring_log_analyst_tool = AgentTool(
    agent=monitoring_log_agent,
    name="gcp_monitoring_log_analyst",
    description="Delegates tasks to the BQ Monitoring Log Agent, a specialist in querying GCP Monitoring Logs in BigQuery. Can list available tables and query them."
)

report_visualizer_tool = AgentTool(
    agent=visualization_agent,
    name="report_visualizer",
    description="Delegates tasks to the Visualization Agent, which takes JSON data and generates visual reports (charts, graphs as SVG or PNG)."
)

# Define the Root Agent
root_agent = Agent(
    model=GEMINI_MODEL_NAME,
    system_prompt=ROOT_AGENT_PROMPT,
    tools=[
        mcp_time_tool, # FunctionTool for direct utility
        audit_log_investigator_tool, # AgentTool for specialist
        monitoring_log_analyst_tool, # AgentTool for specialist
        report_visualizer_tool       # AgentTool for specialist
    ]
)

if __name__ == '__main__':
    print(f"Root Agent (root_agent) has been initialized with model: {GEMINI_MODEL_NAME}.")
    print(f"System Prompt:\n{ROOT_AGENT_PROMPT[:500]}... (truncated)")
    print(f"Tools available: {[tool.name for tool in root_agent.tools]}")
    print("\nTo test interactively, run this agent using 'adk web' or 'adk talk'.")
    print("Ensure the MCP Time Service (Node.js) is running if you plan to test time-related queries.")
    print("Example command: adk talk --agent_path gcp_audit_buddy_agent.root_agent_pkg.agent.root_agent") 