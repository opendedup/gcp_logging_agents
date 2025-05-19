# GCP Audit Buddy Agent

**Version:** 0.1.0
**Description:** GCP Auditing Assistant using Agent Development Kit

GCP Audit Buddy is a sophisticated agent designed to assist with auditing Google Cloud Platform (GCP) environments. It leverages the Google Agent Development Kit (ADK) and utilizes the power of Gemini models to analyze logs, generate reports, and provide insights into your GCP projects.

## Overview

The GCP Audit Buddy system is built around a central `root_agent` that orchestrates a team of specialized sub-agents. This modular design allows for focused analysis and efficient processing of various GCP data sources.

### Core Components

*   **Root Agent (`gcp_audit_buddy_agent`):** The main orchestrator. It receives user queries, determines the best sub-agent(s) to handle the request, and synthesizes the information to provide a comprehensive answer.
*   **Sub-Agents:**
    *   **BQ Audit Log Agent (`audit_log_investigator_tool`):** Specializes in analyzing BigQuery audit logs to track data access, schema changes, and other critical audit events.
    *   **BQ Monitoring Log Agent (`monitoring_log_analyst_tool`):** Focuses on BigQuery monitoring logs to provide insights into query performance, slot utilization, and job statuses.
    *   **Compute Monitoring Log Agent (`compute_log_analyzer_tool`):** Analyzes monitoring logs from Google Compute Engine, providing information on VM performance, network traffic, and other operational metrics.
    *   **Visualization Agent (`report_visualizer_tool`):** Generates visualizations and reports from the data analyzed by other agents. It can create charts and summaries to help understand trends and anomalies.
*   **Tools:**
    *   **MCP Time Service (`mcp_time_tool`):** A utility tool likely used for fetching current timestamps or time-related information, crucial for log analysis and reporting.

## Features

*   **Comprehensive Log Analysis:** Ingests and analyzes various GCP logs, including BigQuery audit logs, BigQuery monitoring logs, and Compute Engine monitoring logs.
*   **Intelligent Orchestration:** The root agent intelligently delegates tasks to specialized sub-agents for efficient and accurate analysis.
*   **Report Generation:** Capable of generating reports and visualizations to summarize findings.
*   **Extensible:** Built with the Google ADK, allowing for potential future expansion with more sub-agents or tools.

## Technical Details

*   **Language:** Python 3.11+
*   **Core Framework:** Google Agent Development Kit (ADK)
*   **AI Model:** Gemini (configurable via `GEMINI_MODEL_NAME` environment variable, defaults to `gemini-1.5-pro-001`)
*   **Key Dependencies:**
    *   `google-adk`
    *   `google-cloud-aiplatform`
    *   `google-genai`
    *   `python-dotenv`
    *   `google-cloud-bigquery`
    *   `matplotlib`
    *   `pandas`
    *   `seaborn`
    *   `svglib`

## Getting Started

To get started with the GCP Audit Buddy Agent, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url> # Replace <repository-url> with the actual URL
    cd gcp-audit-buddy-agent # Or your project's root directory name
    ```
2.  **Set up Python Environment:**
    *   Ensure you have Python 3.11 or newer installed.
    *   It is highly recommended to use a virtual environment:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
3.  **Install Dependencies:**
    *   This project uses Poetry for dependency management. Install Poetry if you haven't already (see [Poetry's official documentation](https://python-poetry.org/docs/#installation)).
    *   Install the project dependencies:
        ```bash
        poetry install
        ```
4.  **Configure Environment Variables:**
    *   Navigate to the `gcp_audit_buddy` directory if you are not already there:
        ```bash
        cd gcp_audit_buddy
        ```
    *   Copy the example environment file to a new `.env` file:
        ```bash
        cp .env.example .env
        ```
    *   Open the `.env` file and update the variables as needed. Key variables include:
        ```env
        GEMINI_MODEL_NAME="gemini-1.5-pro-001" # Or your preferred Gemini model
        # MCP_TIME_SERVICE_URL="http://localhost:3001/time" # Uncomment and set if you run the MCP Time Service locally
        # GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json" # If needed for GCP authentication
        # GCP_PROJECT_ID="your-gcp-project-id" # If needed by agents
        ```
    *   **Note:** The `MCP_TIME_SERVICE_URL` is for the external time service. If you are running it locally (e.g., from the `mcp_time_service` directory in this project), ensure it's started and the URL is correctly configured. The sub-agents might require GCP credentials and a project ID.
5.  **Run the Agent:**

    The agent system consists of two main parts that need to be running:

    *   **Step 1: Start the MCP Time Service (if used locally)**
        *   This service provides time-related information to the agent.
        *   Navigate to the time service directory:
            ```bash
            cd ../mcp_time_service # Assuming you are in gcp_audit_buddy, adjust if necessary
            ```
        *   Start the service (ensure Node.js and npm are installed):
            ```bash
            npm start
            ```
        *   Keep this service running in a separate terminal.
        *   Ensure the `MCP_TIME_SERVICE_URL` in your `gcp_audit_buddy/.env` file points to this service (e.g., `http://localhost:3001/time` if it runs on port 3001).

    *   **Step 2: Run the GCP Audit Buddy Agent**
        *   Navigate to the agent directory (if you are not already there from configuring .env):
            ```bash
            cd ../gcp_audit_buddy # Or the correct path to gcp_audit_buddy directory
            ```
        *   Activate your Python virtual environment if you haven't already:
            ```bash
            source ../.venv/bin/activate # Adjust path if your .venv is elsewhere
            ```
        *   Run the ADK web interface:
            ```bash
            adk web
            ```
        *   This will typically start a local web server where you can interact with the agent.

## Usage

Once the agent is running (both the MCP Time Service, if applicable, and the ADK web interface), you can interact with it by asking questions related to your GCP environment. The root agent will orchestrate with the specialized sub-agents to provide answers.

Here are some example queries you can try:

*   "Can you summarize data access activity for the last 30 minutes?"
*   "Summarize the data in plain English please."
*   "Who was the most active user that is not a service account?"
*   "Can you create a visual report of the activity by admin please?"

Here are a few more examples from another conversation:

*   "Were there any VMs deleted in the last 3 hours?" (This is a duplicate, keeping one instance is fine or I can remove this one if you prefer)
*   "Were there any VMs started in the last 6 hours?"
*   "Check the GCE logs too please."
*   "Can you check and see if there are any VMs that were created in the last hour?"
*   "Tell me as much as you can about the VM."
*   "Do you see any object reads for bucket <the-bucket-name> in the last 24 hours?"

These examples demonstrate the agent's ability to query logs across different services (Compute Engine, BigQuery), summarize information, and generate reports.

## Contributing

(Guidelines for contributing to the project, if applicable.)

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for more details.
