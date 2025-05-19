import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for running in a server environment
import matplotlib.pyplot as plt
import seaborn as sns
import io
from google.generativeai.types import Part, Blob
from typing import Literal

def create_report_visualization(
    data_json_string: str, 
    chart_type: Literal["bar", "line", "pie", "scatter", "histogram"],
    x_column: str, 
    y_column: str, 
    title: str = "Generated Chart", 
    report_format: Literal["svg", "png"] = "svg",
    hue_column: str | None = None # Optional column for color encoding (e.g., in bar or scatter plots)
) -> Part:
    """
    Creates a data visualization from a JSON string and returns it as a Google GenAI Part.

    Args:
        data_json_string: A JSON string representing a list of records (e.g., from a BigQuery query).
        chart_type: The type of chart to generate (e.g., "bar", "line", "pie", "scatter", "histogram").
        x_column: The name of the column to use for the x-axis (or labels for pie chart).
        y_column: The name of the column to use for the y-axis (or values for pie chart/histogram).
        title: The title of the chart.
        report_format: The desired output format ("svg" or "png"). Defaults to "svg".
        hue_column: Optional. The name of the column to use for color encoding (hue) in applicable charts.

    Returns:
        A google.generativeai.types.Part object containing the image data, or a Part with an error message.
    """
    try:
        try:
            data = json.loads(data_json_string)
            if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
                if isinstance(data, dict) and "message" in data and "Query returned no results." in data["message"]:
                     return Part(text=f"Cannot generate chart: {data['message']}")
                if isinstance(data, dict) and "error" in data:
                     return Part(text=f"Cannot generate chart due to upstream error: {data['error']}")
                raise ValueError("Data must be a JSON string representing a list of dictionaries.")
            if not data:
                 return Part(text="Cannot generate chart: Input data is empty.")
            df = pd.DataFrame(data)
        except json.JSONDecodeError:
            return Part(text="Error: Invalid JSON data provided.")
        except ValueError as ve:
            return Part(text=f"Error processing data: {str(ve)}")

        if x_column not in df.columns:
            return Part(text=f"Error: X-axis column '{x_column}' not found in the data. Available columns: {list(df.columns)}")
        if y_column not in df.columns and chart_type != 'histogram': # Histogram only needs one main column for values
            return Part(text=f"Error: Y-axis column '{y_column}' not found in the data. Available columns: {list(df.columns)}")
        if hue_column and hue_column not in df.columns:
            return Part(text=f"Error: Hue column '{hue_column}' not found in the data. Available columns: {list(df.columns)}")

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
                return Part(text=f"Error converting x-column '{x_column}' for plotting: {e}")
        
        try:
            if pd.api.types.is_numeric_dtype(df[y_column]):
                pass # Already numeric
            else:
                df[y_column] = pd.to_numeric(df[y_column])
        except Exception as e:
            return Part(text=f"Error converting y-column '{y_column}' to numeric for plotting: {e}")

        if chart_type == "bar":
            sns.barplot(x=df[x_column], y=df[y_column], hue=df[hue_column] if hue_column else None)
            plt.xticks(rotation=45, ha='right')
        elif chart_type == "line":
            sns.lineplot(x=df[x_column], y=df[y_column], hue=df[hue_column] if hue_column else None, marker='o')
            plt.xticks(rotation=45, ha='right')
        elif chart_type == "pie":
            if not pd.api.types.is_numeric_dtype(df[y_column]):
                 return Part(text=f"Error: For pie chart, y-column '{y_column}' must be numeric.")
            # Ensure we don't have too many slices for a pie chart
            if len(df[x_column].unique()) > 15:
                 return Part(text=f"Error: Too many unique values in x-column '{x_column}' ({len(df[x_column].unique())}) for a pie chart. Please choose a different chart type or filter data.")
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
            return Part(text=f"Error: Unsupported chart type '{chart_type}'. Supported types: bar, line, pie, scatter, histogram.")

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
            return Part(text=f"Error: Unsupported report format '{report_format}'. Supported formats: svg, png.")
        
        img_buffer.seek(0)
        image_bytes = img_buffer.getvalue()
        plt.close() # Close the plot to free up memory

        return Part(inline_data=Blob(mime_type=mime_type, data=image_bytes))

    except Exception as e:
        # Ensure plot is closed if an unexpected error occurs mid-process
        plt.close()
        return Part(text=f"An unexpected error occurred while creating the visualization: {str(e)}")

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
    # bar_chart_part = create_report_visualization(sample_json_string, "bar", "category", "value", "Sample Bar Chart", "svg", hue_column="group")
    # if bar_chart_part.text:
    #     print(f"Error: {bar_chart_part.text}")
    # elif bar_chart_part.inline_data:
    #     print(f"Bar chart generated successfully. MimeType: {bar_chart_part.inline_data.mime_type}, Size: {len(bar_chart_part.inline_data.data)} bytes")
    #     # with open("bar_chart_test.svg", "wb") as f:
    #     #     f.write(bar_chart_part.inline_data.data)
    #     # print("Saved to bar_chart_test.svg")

    # Test Pie Chart
    print("\nTesting Pie Chart (PNG)...")
    # To make pie chart meaningful, let's sum values by category first or use appropriate data
    # df_sample = pd.DataFrame(sample_data_list)
    # pie_data = df_sample.groupby('category')['value'].sum().reset_index()
    # pie_json_string = pie_data.to_json(orient='records')
    # pie_chart_part = create_report_visualization(pie_json_string, "pie", "category", "value", "Sample Pie Chart", "png")
    # if pie_chart_part.text:
    #     print(f"Error: {pie_chart_part.text}")
    # elif pie_chart_part.inline_data:
    #     print(f"Pie chart generated successfully. MimeType: {pie_chart_part.inline_data.mime_type}, Size: {len(pie_chart_part.inline_data.data)} bytes")
        # with open("pie_chart_test.png", "wb") as f:
        #     f.write(pie_chart_part.inline_data.data)
        # print("Saved to pie_chart_test.png")

    # Test with non-existent column
    print("\nTesting Non-Existent Column...")
    # error_part = create_report_visualization(sample_json_string, "bar", "non_existent_col", "value")
    # if error_part.text:
    #     print(f"Caught expected error: {error_part.text}")

    # Test with empty data
    print("\nTesting Empty Data...")
    # empty_data_part = create_report_visualization("[]", "bar", "category", "value")
    # if empty_data_part.text:
    #     print(f"Caught expected error for empty data: {empty_data_part.text}")

    # Test with no results data
    print("\nTesting No Results Data...")
    # no_results_data = json.dumps({"message": "Query returned no results."})
    # no_results_part = create_report_visualization(no_results_data, "bar", "category", "value")
    # if no_results_part.text:
    #     print(f"Caught expected error for no results data: {no_results_part.text}")

    print("\nTo fully test, uncomment example calls and optionally save the output to files.")
    print("Ensure matplotlib, seaborn, and pandas are installed.") 