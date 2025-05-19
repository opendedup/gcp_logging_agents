#!/bin/bash

# --- Configuration ---
PROJECT_ID="lemmingsinthewind"
DATASET_ID="overwatch_log"
OUTPUT_DIR="schemas/overwatch_logs" # Note: Changed from overwatch_log to overwatch_logs as requested

# --- Script Logic ---

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Error: Could not create output directory '$OUTPUT_DIR'."
    exit 1
fi

echo "Fetching table list from $PROJECT_ID:$DATASET_ID..."

# Get table names using bq ls and jq
# The `readarray -t` populates an array, handling potential (though unlikely for BQ)
# spaces in names and removing newlines from each element.
# `jq -r '.[].tableReference.tableId'` extracts the tableId from the JSON output of `bq ls`.
readarray -t table_names < <(bq ls --format=json "$PROJECT_ID:$DATASET_ID" | jq -r '.[].tableReference.tableId')

# Check if any tables were found
if [ ${#table_names[@]} -eq 0 ]; then
    echo "No tables found in $PROJECT_ID:$DATASET_ID or error fetching tables."
    # You can check bq's exit code or stderr from the command above if needed for more detailed error handling
    exit 1
fi

echo "Found ${#table_names[@]} tables. Dumping schemas to '$OUTPUT_DIR'..."

# Loop through each table name
for table_name in "${table_names[@]}"; do
    if [ -z "$table_name" ]; then # Skip if table_name is empty (shouldn't happen with jq)
        continue
    fi

    echo "  Dumping schema for table: $table_name"
    output_file="$OUTPUT_DIR/${table_name}.json"
    full_table_id="$PROJECT_ID:$DATASET_ID.$table_name"

    # Get the schema and save it
    if bq show --schema --format=prettyjson "$full_table_id" > "$output_file"; then
        echo "    Schema saved to $output_file"
    else
        echo "    ERROR: Failed to get schema for $full_table_id. Check bq output."
        # Optionally, remove the potentially empty/failed file
        # rm -f "$output_file"
    fi
done

echo "All done. Schemas are in $OUTPUT_DIR"