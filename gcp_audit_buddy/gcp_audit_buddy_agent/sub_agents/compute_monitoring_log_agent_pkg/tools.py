import json
import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GCP configuration from environment variables
GCP_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-gcp-project-id")
COMPUTE_MONITORING_LOGS_FULL_DATASET_ID = os.getenv("COMPUTE_MONITORING_LOGS_FULL_DATASET_ID", "your-gcp-project-id.your-dataset-name")

# Specific tables for compute monitoring
COMPUTE_TABLE_NAMES = [
    "GCEGuestAgent",
    "GCEGuestAgentManager",
    "OSConfigAgent",
]

# Fully qualified table names
FULLY_QUALIFIED_COMPUTE_TABLES = [
    f"{COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}.{table_name}" for table_name in COMPUTE_TABLE_NAMES
]

def list_compute_monitoring_log_tables() -> str:
    """
    Lists the predefined GCP compute monitoring log BigQuery tables.

    The tables are:
    - {COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}.GCEGuestAgent
    - {COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}.GCEGuestAgentManager
    - {COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}.OSConfigAgent

    Returns:
        A JSON string representing a list of fully qualified table IDs.
    """
    try:
        return json.dumps(FULLY_QUALIFIED_COMPUTE_TABLES)
    except Exception as e:
        error_message = f"An error occurred while constructing the list of compute monitoring tables: {str(e)}"
        print(error_message)
        return json.dumps({"error": "Failed to list compute monitoring tables.", "details": str(e)})

def query_gcp_compute_monitoring_logs(sql_query: str) -> str:
    """
    Executes a SQL query against Google Cloud BigQuery, targeting specific compute monitoring log tables,
    and returns the results as a JSON string.

    Args:
        sql_query: The SQL query string to execute. The query should target one of the compute monitoring tables:
                   GCEGuestAgent, GCEGuestAgentManager, or OSConfigAgent within the
                   `{COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}` dataset.
                   Use `list_compute_monitoring_log_tables` to see the exact table names.
                   Example: SELECT * FROM `{COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}.GCEGuestAgent` LIMIT 10

    Returns:
        A JSON string representing the query results, or an error message if the query fails.
    """
    try:
        client = bigquery.Client()
        print(f"Executing BQ Compute Monitoring Log Query: {sql_query}")
        
        # Basic validation to ensure the query targets one of the allowed tables
        # This is a simple check and might need to be more robust depending on query complexity
        targeted_table_is_valid = False
        for allowed_table in FULLY_QUALIFIED_COMPUTE_TABLES:
            if f"`{allowed_table}`" in sql_query or f" {allowed_table} " in sql_query:
                 targeted_table_is_valid = True
                 break
        
        if not targeted_table_is_valid:
             error_msg = f"Query must target one of the allowed compute monitoring tables: {FULLY_QUALIFIED_COMPUTE_TABLES}. Your query: {sql_query}"
             print(error_msg)
             return json.dumps({"error": "Invalid query target.", "details": error_msg})

        query_job = client.query(sql_query)
        results = query_job.result()

        rows = [dict(row) for row in results]
        
        for row in rows:
            for key, value in row.items():
                if hasattr(value, 'isoformat'): # Convert datetime objects to ISO format strings
                    row[key] = value.isoformat()

        if not rows:
            return json.dumps({"message": "Query returned no results."})
        
        return json.dumps(rows)

    except Exception as e:
        error_message = f"An error occurred while querying BigQuery compute monitoring logs: {str(e)}"
        print(error_message)
        return json.dumps({"error": "Failed to execute BigQuery query.", "details": str(e)})

if __name__ == '__main__':
    print("Testing Compute Monitoring Log Tools...")
    print(f"Configured Compute Monitoring Dataset: {COMPUTE_MONITORING_LOGS_FULL_DATASET_ID}")
    print(f"Known tables: {FULLY_QUALIFIED_COMPUTE_TABLES}")

    print("\nListing compute monitoring tables...")
    table_list_json = list_compute_monitoring_log_tables()
    print(table_list_json)
    


    print("\nTo fully test, uncomment the example query usage, ensure your .env is configured,")
    print("that the specified dataset and tables exist, and you have permissions.") 