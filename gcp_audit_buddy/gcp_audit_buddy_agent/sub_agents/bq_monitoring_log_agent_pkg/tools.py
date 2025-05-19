import json
import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GCP configuration from environment variables
GCP_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-gcp-project-id")
# GCP_MONITORING_LOGS_DATASET from .env is expected to be like "project.dataset_name"
MONITORING_LOGS_FULL_DATASET_ID = os.getenv("GCP_MONITORING_LOGS_DATASET", f"{GCP_PROJECT_ID}.your_monitoring_dataset")

def list_monitoring_log_tables() -> str:
    """
    Lists all tables in the configured GCP monitoring logs BigQuery dataset.

    The monitoring logs dataset is determined by the GCP_MONITORING_LOGS_DATASET environment variable.

    Returns:
        A JSON string representing a list of table IDs (e.g., ["table1", "table2"]),
        or an error message if listing fails.
    """
    try:
        client = bigquery.Client()
        # Dataset ID in BigQuery client does not include the project ID if client is project-aware
        # However, MONITORING_LOGS_FULL_DATASET_ID is expected to be "project.dataset"
        # We need to parse it for the client.list_tables() method.
        if '.' not in MONITORING_LOGS_FULL_DATASET_ID:
            raise ValueError(f"GCP_MONITORING_LOGS_DATASET environment variable '{MONITORING_LOGS_FULL_DATASET_ID}' is not in the expected 'project.dataset' format.")
        
        dataset_ref = bigquery.DatasetReference.from_string(MONITORING_LOGS_FULL_DATASET_ID, default_project=client.project)

        tables = list(client.list_tables(dataset_ref))

        if not tables:
            return json.dumps({"message": f"No tables found in dataset '{MONITORING_LOGS_FULL_DATASET_ID}'."})

        table_ids = [table.table_id for table in tables]
        return json.dumps(table_ids)

    except Exception as e:
        error_message = f"An error occurred while listing tables in BigQuery dataset '{MONITORING_LOGS_FULL_DATASET_ID}': {str(e)}"
        print(error_message)
        return json.dumps({"error": "Failed to list BigQuery tables.", "details": str(e)})

def query_gcp_monitoring_logs(sql_query: str) -> str:
    """
    Executes a SQL query against Google Cloud BigQuery, targeting monitoring log tables,
    and returns the results as a JSON string.

    Args:
        sql_query: The SQL query string to execute. The query should be written to target
                   tables within the monitoring logs dataset (e.g., `lemmingsinthewind.overwatch_log.some_monitoring_table`).
                   Use the `list_monitoring_log_tables` tool to discover available tables.

    Returns:
        A JSON string representing the query results, or an error message if the query fails.
    """
    try:
        client = bigquery.Client()
        print(f"Executing BQ Monitoring Log Query: {sql_query}")
        query_job = client.query(sql_query)
        results = query_job.result()

        rows = [dict(row) for row in results]
        
        for row in rows:
            for key, value in row.items():
                if hasattr(value, 'isoformat'):
                    row[key] = value.isoformat()

        if not rows:
            return json.dumps({"message": "Query returned no results."})
        
        return json.dumps(rows)

    except Exception as e:
        error_message = f"An error occurred while querying BigQuery monitoring logs: {str(e)}"
        print(error_message)
        return json.dumps({"error": "Failed to execute BigQuery query.", "details": str(e)})

if __name__ == '__main__':
    print("Testing Monitoring Log Tools...")
    print(f"Configured Monitoring Dataset: {MONITORING_LOGS_FULL_DATASET_ID}")
    
    print("\nAttempting to list tables...")
    # table_list_json = list_monitoring_log_tables()
    # print(table_list_json)
    # tables_data = json.loads(table_list_json)
    # if "error" not in tables_data and tables_data and isinstance(tables_data, list) and len(tables_data) > 0:
    #     first_table = tables_data[0]
    #     test_query = f"SELECT * FROM `{MONITORING_LOGS_FULL_DATASET_ID}.{first_table}` LIMIT 2"
    #     print(f"\nAttempting to query first table: {first_table} with query: {test_query}")
    #     query_results = query_gcp_monitoring_logs(test_query)
    #     print(query_results)
    # elif "error" in tables_data:
    #     print(f"Error listing tables: {tables_data['error']}")
    # elif not tables_data or not isinstance(tables_data, list) or len(tables_data) == 0:
    #     print("No tables found or tables_data is not a list or is empty.")
    # else:
    #     print("No tables to query or an issue occurred.")

    print("\nTo fully test, uncomment the example usage, ensure your .env is configured,")
    print("that the specified dataset exists, contains tables, and you have permissions.")
    print("Example query uses environment variables for project and dataset.") 