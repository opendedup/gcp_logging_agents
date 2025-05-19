# gcp_audit_buddy_agent/__init__.py

# Import and expose the main root_agent so it can be easily discovered by ADK tools.
# This allows you to run commands like:
# adk talk --agent_path gcp_audit_buddy_agent.root_agent
# or select it in the ADK Web UI via the path gcp_audit_buddy_agent.root_agent

import os

from . import agent

__all__ = ["agent"]
