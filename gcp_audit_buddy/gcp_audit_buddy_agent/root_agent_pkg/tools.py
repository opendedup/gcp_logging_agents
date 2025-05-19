import os
import requests
import json
from dotenv import load_dotenv
from typing import Dict, Union

# Load environment variables from .env file
load_dotenv()

# Get the MCP Time Service URL from environment variables
# Ensure this is uncommented and correctly set in your .env file (e.g., http://localhost:3001/time)
MCP_TIME_SERVICE_BASE_URL = os.getenv("MCP_TIME_SERVICE_URL")

def call_mcp_time_service(offset_hours: int = 0) -> Dict[str, Union[str, int, Dict]]:
    """
    Calls the external MCP Time Service to get the current GMT time, optionally with an offset.

    Args:
        offset_hours: An optional integer representing the number of hours to offset from current GMT.
                      Positive values are future, negative values are past. Defaults to 0.

    Returns:
        A dictionary containing the GMT time and offset applied, e.g.:
        {"gmt_time": "YYYY-MM-DDTHH:MM:SSZ", "offset_applied_hours": offset_hours}
        or an error dictionary if the call fails, e.g.:
        {"error": "MCP Time Service call failed", "details": "..."}
    """
    if not MCP_TIME_SERVICE_BASE_URL:
        error_msg = "MCP_TIME_SERVICE_URL is not set in the environment variables (.env file)."
        print(f"Error: {error_msg}")
        return {"error": "Configuration error", "details": error_msg}

    try:
        # Construct the full URL with query parameters
        url = f"{MCP_TIME_SERVICE_BASE_URL}?offset_hours={offset_hours}"
        
        print(f"Calling MCP Time Service: {url}")
        response = requests.get(url, timeout=5) # 5-second timeout
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        
        time_data = response.json()
        # Ensure the expected keys are present, though the service should be consistent
        if "gmt_time" not in time_data or "offset_applied_hours" not in time_data:
            return {"error": "MCP Time Service returned unexpected data format.", "details": str(time_data)}
        
        return time_data

    except requests.exceptions.Timeout:
        error_msg = f"MCP Time Service call timed out at {MCP_TIME_SERVICE_BASE_URL}"
        print(f"Error: {error_msg}")
        return {"error": "MCP Time Service call failed", "details": error_msg}
    except requests.exceptions.ConnectionError:
        error_msg = f"Could not connect to MCP Time Service at {MCP_TIME_SERVICE_BASE_URL}. Please ensure it is running."
        print(f"Error: {error_msg}")
        return {"error": "MCP Time Service call failed", "details": error_msg}
    except requests.exceptions.RequestException as e:
        error_msg = f"An error occurred while calling MCP Time Service: {str(e)}"
        print(f"Error: {error_msg}")
        return {"error": "MCP Time Service call failed", "details": error_msg}
    except json.JSONDecodeError:
        error_msg = "Failed to decode JSON response from MCP Time Service."
        print(f"Error: {error_msg}")
        return {"error": "MCP Time Service call failed", "details": error_msg}

if __name__ == '__main__':
    print("Testing MCP Time Service call...")
    
    if not MCP_TIME_SERVICE_BASE_URL:
        print("MCP_TIME_SERVICE_URL not set. Please set it in your .env file (e.g., MCP_TIME_SERVICE_URL=http://localhost:3001/time) and ensure the service is running.")
    else:
        print(f"Using MCP Time Service URL: {MCP_TIME_SERVICE_BASE_URL}")
        
        # Test with default offset
        print("\nTesting with offset_hours = 0 (default):")
        # result_default = call_mcp_time_service()
        # print(result_default)

        # Test with a positive offset
        print("\nTesting with offset_hours = 2:")
        # result_positive_offset = call_mcp_time_service(offset_hours=2)
        # print(result_positive_offset)

        # Test with a negative offset
        print("\nTesting with offset_hours = -5:")
        # result_negative_offset = call_mcp_time_service(offset_hours=-5)
        # print(result_negative_offset)
        
        print("\nTo run these tests, uncomment the call_mcp_time_service() lines.")
        print("Ensure the MCP Time Service (Node.js server) is running and MCP_TIME_SERVICE_URL is correctly set in .env.") 