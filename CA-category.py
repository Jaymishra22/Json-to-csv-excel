import os
import json
import pandas as pd


def flatten_json(data):
    flattened_data = {}

    def flatten_helper(current_dict, key_name=""):
        if isinstance(current_dict, dict):
            for key, value in current_dict.items():
                new_key = f"{key_name}.{key}" if key_name else key
                flatten_helper(value, new_key)
        elif isinstance(current_dict, list):
            for i, item in enumerate(current_dict):
                new_key = f"{key_name}.{i}" if key_name else str(i)
                flatten_helper(item, new_key)
        else:
            flattened_data[key_name] = current_dict

    flatten_helper(data)
    return flattened_data


# Load JSON data from file
with open("CA_category_id.json", "r") as file:
    json_data = json.load(file)

# Flatten the JSON data
flattened_data = flatten_json(json_data)

# Convert flattened data to DataFrame
df = pd.DataFrame(flattened_data.items(), columns=['Key', 'Value'])

# Create a directory if it doesn't exist
directory = "csv_files"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save DataFrame to CSV file inside the "csv_files" folder
csv_file_path = os.path.join(directory, "flattened_data.csv")
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")
