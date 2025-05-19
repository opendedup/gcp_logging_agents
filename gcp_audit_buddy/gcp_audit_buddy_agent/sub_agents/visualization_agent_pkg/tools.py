import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for running in a server environment
import matplotlib.pyplot as plt
import seaborn as sns
import io
from google.genai.types import Part, Blob
import base64
from typing import Literal, Optional

def create_report_visualization(
    data_json_string: str, 
    chart_type: Literal["bar", "line", "pie", "scatter", "histogram"],
    x_column: str, 
    y_column: str, 
    title: str = "Generated Chart", 
    report_format: Literal["svg", "png"] = "svg",
    hue_column: Optional[str] = None # Optional column for color encoding (e.g., in bar or scatter plots)
) -> dict:
    """
    Creates a data visualization from a JSON string and returns it as a dictionary
    containing base64 encoded image data and mime type.

    Args:
        data_json_string: A JSON string representing a list of records (e.g., from a BigQuery query).
        chart_type: The type of chart to generate (e.g., "bar", "line", "pie", "scatter", "histogram").
        x_column: The name of the column to use for the x-axis (or labels for pie chart).
        y_column: The name of the column to use for the y-axis (or values for pie chart/histogram).
        title: The title of the chart.
        report_format: The desired output format ("svg" or "png"). Defaults to "svg".
        hue_column: Optional. The name of the column to use for color encoding (hue) in applicable charts.

    Returns:
        A dictionary with "mime_type", "image_data_base64", and "filename_suggestion" on success,
        or a dictionary with "error" on failure.
    """
    try:
        try:
            data = json.loads(data_json_string)
            if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
                if isinstance(data, dict) and "message" in data and "Query returned no results." in data["message"]:
                     return {"error": f"Cannot generate chart: {data['message']}"}
                if isinstance(data, dict) and "error" in data:
                     return {"error": f"Cannot generate chart due to upstream error: {data['error']}"}
                raise ValueError("Data must be a JSON string representing a list of dictionaries.")
            if not data:
                 return {"error": "Cannot generate chart: Input data is empty."}
            df = pd.DataFrame(data)
        except json.JSONDecodeError:
            return {"error": "Error: Invalid JSON data provided."}
        except ValueError as ve:
            return {"error": f"Error processing data: {str(ve)}"}

        if x_column not in df.columns:
            return {"error": f"Error: X-axis column '{x_column}' not found in the data. Available columns: {list(df.columns)}"}
        if y_column not in df.columns and chart_type != 'histogram': # Histogram only needs one main column for values
            return {"error": f"Error: Y-axis column '{y_column}' not found in the data. Available columns: {list(df.columns)}"}
        if hue_column and hue_column not in df.columns:
            return {"error": f"Error: Hue column '{hue_column}' not found in the data. Available columns: {list(df.columns)}"}

        plt.figure(figsize=(10, 6))
        sns.set_theme(style="whitegrid")

        # Ensure numeric conversion for plotting where appropriate, handle errors
        if chart_type not in ['histogram']:
            try:
                if x_column and pd.api.types.is_numeric_dtype(df[x_column]):
                    pass # Already numeric
                elif x_column and pd.api.types.is_datetime64_any_dtype(df[x_column]):
                    df[x_column] = pd.to_datetime(df[x_column]) # Ensure it's datetime if it looks like it
                # For other types, keep as is, Seaborn might handle it or it's categorical
            except Exception as e:
                return {"error": f"Error converting x-column '{x_column}' for plotting: {e}"}
        
        try:
            if pd.api.types.is_numeric_dtype(df[y_column]):
                pass # Already numeric
            else:
                df[y_column] = pd.to_numeric(df[y_column])
        except Exception as e:
            return {"error": f"Error converting y-column '{y_column}' to numeric for plotting: {e}"}

        if chart_type == "bar":
            sns.barplot(x=df[x_column], y=df[y_column], hue=df[hue_column] if hue_column else None)
            plt.xticks(rotation=45, ha='right')
        elif chart_type == "line":
            sns.lineplot(x=df[x_column], y=df[y_column], hue=df[hue_column] if hue_column else None, marker='o')
            plt.xticks(rotation=45, ha='right')
        elif chart_type == "pie":
            if not pd.api.types.is_numeric_dtype(df[y_column]):
                 return {"error": f"Error: For pie chart, y-column '{y_column}' must be numeric."}
            # Ensure we don't have too many slices for a pie chart
            if len(df[x_column].unique()) > 15:
                 return {"error": f"Error: Too many unique values in x-column '{x_column}' ({len(df[x_column].unique())}) for a pie chart. Please choose a different chart type or filter data."}
            plt.pie(df[y_column], labels=df[x_column], autopct='%1.1f%%', startangle=90)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        elif chart_type == "scatter":
            sns.scatterplot(x=df[x_column], y=df[y_column], hue=df[hue_column] if hue_column else None)
            plt.xticks(rotation=45, ha='right')
        elif chart_type == "histogram":
            # For histogram, y_column is actually the column whose distribution we want to see.
            # x_column might not be explicitly used by sns.histplot if y_column is specified for values.
            sns.histplot(data=df, x=y_column, hue=hue_column if hue_column else None, kde=True)
        else:
            return {"error": f"Error: Unsupported chart type '{chart_type}'. Supported types: bar, line, pie, scatter, histogram."}

        plt.title(title)
        plt.tight_layout() # Adjust layout to prevent labels from being cut off

        img_buffer = io.BytesIO()
        if report_format == "svg":
            plt.savefig(img_buffer, format="svg")
            mime_type = "image/svg+xml"
        elif report_format == "png":
            plt.savefig(img_buffer, format="png")
            mime_type = "image/png"
        else:
            plt.close()
            return {"error": f"Error: Unsupported report format '{report_format}'. Supported formats: svg, png."}
        
        img_buffer.seek(0)
        image_bytes = img_buffer.getvalue()
        plt.close() # Close the plot to free up memory

        image_data_base64 = base64.b64encode(image_bytes).decode('utf-8')
        filename_suggestion = f"{title.replace(' ', '_').lower().replace('[^a-z0-9_]', '')}.{report_format}"

        return {
            "mime_type": mime_type,
            "image_data_base64": image_data_base64,
            "filename_suggestion": filename_suggestion
        }

    except Exception as e:
        # Ensure plot is closed if an unexpected error occurs mid-process
        plt.close()
        return {"error": f"An unexpected error occurred while creating the visualization: {str(e)}"}

if __name__ == '__main__':
    # Example usage:
    sample_data_list = [
        {"category": "A", "value": 30, "group": "X"},
        {"category": "B", "value": 50, "group": "X"},
        {"category": "C", "value": 20, "group": "Y"},
        {"category": "A", "value": 40, "group": "Y"},
        {"category": "B", "value": 25, "group": "X"}
    ]
    sample_json_string = json.dumps(sample_data_list)

    print(f"Testing with sample data: {sample_json_string}")

    # Test Bar Chart
    print("\nTesting Bar Chart (SVG)...")
    bar_chart_result = create_report_visualization(sample_json_string, "bar", "category", "value", "Sample Bar Chart", "svg", hue_column="group")
    if "error" in bar_chart_result:
        print(f"Error: {bar_chart_result['error']}")
    else:
        print(f"Bar chart generated successfully. MimeType: {bar_chart_result['mime_type']}, Base64 Length: {len(bar_chart_result['image_data_base64'])}, Filename: {bar_chart_result['filename_suggestion']}")
        # with open(bar_chart_result['filename_suggestion'], "wb") as f:
        #     f.write(base64.b64decode(bar_chart_result['image_data_base64']))
        # print(f"Saved to {bar_chart_result['filename_suggestion']}")

    # Test Pie Chart
    print("\nTesting Pie Chart (PNG)...")
    df_sample = pd.DataFrame(sample_data_list)
    pie_data = df_sample.groupby('category')['value'].sum().reset_index()
    pie_json_string = pie_data.to_json(orient='records')
    pie_chart_result = create_report_visualization(pie_json_string, "pie", "category", "value", "Sample Pie Chart", "png")
    if "error" in pie_chart_result:
        print(f"Error: {pie_chart_result['error']}")
    else:
        print(f"Pie chart generated successfully. MimeType: {pie_chart_result['mime_type']}, Base64 Length: {len(pie_chart_result['image_data_base64'])}, Filename: {pie_chart_result['filename_suggestion']}")
        # with open(pie_chart_result['filename_suggestion'], "wb") as f:
        #     f.write(base64.b64decode(pie_chart_result['image_data_base64']))
        # print(f"Saved to {pie_chart_result['filename_suggestion']}")

    # Test with non-existent column
    print("\nTesting Non-Existent Column...")
    error_result_col = create_report_visualization(sample_json_string, "bar", "non_existent_col", "value")
    if "error" in error_result_col:
        print(f"Caught expected error: {error_result_col['error']}")

    # Test with empty data
    print("\nTesting Empty Data...")
    empty_data_result = create_report_visualization("[]", "bar", "category", "value")
    if "error" in empty_data_result:
        print(f"Caught expected error for empty data: {empty_data_result['error']}")

    # Test with no results data
    print("\nTesting No Results Data...")
    no_results_data = json.dumps({"message": "Query returned no results."})
    no_results_result = create_report_visualization(no_results_data, "bar", "category", "value")
    if "error" in no_results_result:
        print(f"Caught expected error for no results data: {no_results_result['error']}")

    print("\nTo fully test, uncomment example calls and optionally save the output to files.")
    print("Ensure matplotlib, seaborn, and pandas are installed.") 