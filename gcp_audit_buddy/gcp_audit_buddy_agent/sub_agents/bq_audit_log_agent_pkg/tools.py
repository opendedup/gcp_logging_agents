import json
from google.cloud import bigquery
from google.oauth2 import service_account
import os

def query_gcp_audit_logs(sql_query: str) -> str:
    """
    Executes a SQL query against Google Cloud BigQuery and returns the results as a JSON string.

    Args:
        sql_query: The SQL query string to execute. 
                   The query should be written to target the correct audit log tables,
                   e.g., `lemmingsinthewind.overwatch_audit.cloudaudit_googleapis_com_activity`
                   or `lemmingsinthewind.overwatch_audit.cloudaudit_googleapis_com_data_access`.

    Returns:
        A JSON string representing the query results, or an error message if the query fails.
    """
    try:
        # Ensure GOOGLE_APPLICATION_CREDENTIALS is set if using service account,
        # otherwise relies on Application Default Credentials (ADC)
        # For ADC to work, you must be authenticated (e.g., via `gcloud auth application-default login`)
        client = bigquery.Client()

        print(f"Executing BQ Audit Log Query: {sql_query}")
        query_job = client.query(sql_query)  # Make an API request.
        results = query_job.result()  # Wait for the job to complete.

        # Convert results to a list of dictionaries
        rows = [dict(row) for row in results]
        
        # Convert datetime objects to ISO format strings for JSON serialization
        for row in rows:
            for key, value in row.items():
                if hasattr(value, 'isoformat'): # Checks for datetime, date, time objects
                    row[key] = value.isoformat()

        if not rows:
            return json.dumps({"message": "Query returned no results."})
        
        return json.dumps(rows)

    except Exception as e:
        error_message = f"An error occurred while querying BigQuery audit logs: {str(e)}"
        print(error_message)
        # Consider how much detail to expose. For now, returning a generic error to the agent.
        return json.dumps({"error": "Failed to execute BigQuery query.", "details": str(e)})

if __name__ == '__main__':
    # Example Usage (requires BigQuery table to exist and appropriate auth)
    # Replace with your actual project, dataset, and table and ensure ADC is set up.
    
    # NOTE: THIS EXAMPLE WILL LIKELY FAIL IF YOU RUN IT DIRECTLY WITHOUT CONFIGURING
    # THE TABLES AND AUTH PROPERLY. IT IS HERE FOR ILLUSTRATION.

    # Make sure your .env file reflects the correct dataset:
    # GCP_AUDIT_LOGS_DATASET="lemmingsinthewind.overwatch_audit"
    
    # Example query (adjust table names and conditions as needed):
    test_query_activity = f"""
    SELECT
        protopayload_auditlog.methodName,
        protopayload_auditlog.resourceName,
        protopayload_auditlog.authenticationInfo.principalEmail AS principalEmail,
        timestamp
    FROM
        `{os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")}.{os.getenv("GCP_AUDIT_LOGS_DATASET", "your_dataset")}.cloudaudit_googleapis_com_activity`
    WHERE
        protopayload_auditlog.methodName = "v1.compute.instances.delete"
    ORDER BY
        timestamp DESC
    LIMIT 10
    """

    test_query_data_access = f"""
    SELECT
        protopayload_auditlog.methodName,
        protopayload_auditlog.resourceName,
        protopayload_auditlog.authenticationInfo.principalEmail AS principalEmail,
        timestamp
    FROM
        `{os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")}.{os.getenv("GCP_AUDIT_LOGS_DATASET", "your_dataset")}.cloudaudit_googleapis_com_data_access`
    WHERE
        resource.type = "bigquery_dataset"
    ORDER BY
        timestamp DESC
    LIMIT 10
    """

    test_query_system_event = f"""
    SELECT
        timestamp, # Or the main timestamp field in system_event
        protopayload_auditlog.serviceName, # Example field
        protopayload_auditlog.methodName,  # Example field
        protopayload_auditlog.resourceName # Example field
        # Add other relevant fields from system_event schema here
    FROM
        `{os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")}.{os.getenv("GCP_AUDIT_LOGS_DATASET", "your_dataset")}.cloudaudit_googleapis_com_system_event`
    WHERE
        protopayload_auditlog.serviceName = 'k8s.io' # Example filter, adjust as needed
    ORDER BY
        timestamp DESC # Or the main timestamp field
    LIMIT 5
    """
    
    print("Testing activity log query...")
    # To run this, you'd need to set up python-dotenv to load .env or set env vars manually
    # from dotenv import load_dotenv
    # load_dotenv()
    # results_activity = query_gcp_audit_logs(test_query_activity)
    # print(results_activity)

    # print("\nTesting data access log query...")
    # results_data_access = query_gcp_audit_logs(test_query_data_access)
    # print(results_data_access)

    print("\nTesting system event log query...")
    # results_system_event = query_gcp_audit_logs(test_query_system_event)
    # print(results_system_event)
    
    print("\nTo fully test, uncomment the dotenv lines, ensure your .env is configured,")
    print("and that the specified tables exist and you have permissions.")
    print("Example queries use environment variables for project and dataset.")
    print("You might need to install python-dotenv: pip install python-dotenv") 