import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool

# Import the root agent's prompt and its direct tools
from .prompts import ROOT_AGENT_PROMPT
from .tools import call_mcp_time_service

# Import the specialist sub-agents
# These paths are relative to the current gcp_audit_buddy_agent package
from .sub_agents.bq_audit_log_agent_pkg.agent import audit_log_agent
from .sub_agents.bq_monitoring_log_agent_pkg.agent import monitoring_log_agent
from .sub_agents.visualization_agent_pkg.agent import visualization_agent
from .sub_agents.compute_monitoring_log_agent_pkg.agent import compute_monitoring_log_agent

# Load environment variables from .env file
load_dotenv()

# Get the Gemini model name from environment variable, with a default
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro-001")

# Create a FunctionTool for the MCP Time Service
mcp_time_tool = FunctionTool(
    func=call_mcp_time_service,
)

# Create AgentTools for the specialist sub-agents
# The names here MUST match the names used in the ROOT_AGENT_PROMPT
audit_log_investigator_tool = AgentTool(
    agent=audit_log_agent,)

monitoring_log_analyst_tool = AgentTool(
    agent=monitoring_log_agent)

report_visualizer_tool = AgentTool(
    agent=visualization_agent)

# Added new AgentTool for Compute Monitoring Logs
compute_log_analyzer_tool = AgentTool(
    agent=compute_monitoring_log_agent)

# Define the Root Agent
root_agent = Agent(
    model=GEMINI_MODEL_NAME,
    name="gcp_audit_buddy_agent",
    description="The main agent that orchestrates the GCP Audit Buddy system. It uses the MCP Time Service, the BQ Audit Log Agent, the BQ Monitoring Log Agent, the Compute Monitoring Log Agent, and the Visualization Agent to answer questions and provide reports.",
    instruction=ROOT_AGENT_PROMPT,
    tools=[
        mcp_time_tool, # FunctionTool for direct utility
        audit_log_investigator_tool, # AgentTool for specialist
        monitoring_log_analyst_tool, # AgentTool for specialist
        compute_log_analyzer_tool,   # AgentTool for specialist (New)
        report_visualizer_tool       # AgentTool for specialist
    ]
)