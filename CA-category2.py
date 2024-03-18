import os
import pandas as pd
# Read the CSV file into a pandas DataFrame
df = pd.read_csv("csv_files/flattened_data.csv")

# Create a directory for Excel files if it doesn't exist
excel_directory = "excel_files"
if not os.path.exists(excel_directory):
    os.makedirs(excel_directory)

# Define the path for the Excel file
excel_file_path = os.path.join(excel_directory, "flattened_data.xlsx")

# Convert DataFrame to Excel file
df.to_excel(excel_file_path, index=False)

print(f"Excel file saved at: {excel_file_path}")
