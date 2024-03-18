import json
import csv
import pandas as pd

# Read the JSON file
with open('C:\\Users\\dell\\Desktop\\Youtube data set\\'
          'CA_category_id.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract required fields and prepare data for CSV
csv_data = []
for item in data['items']:
    csv_row = {
        'kind': item['kind'],
        'etag': item['etag'],
        'id': item['id'],
        'channelId': item['snippet']['channelId'],
        'assignable': item['snippet']['assignable'],
        'title': item['snippet']['title']
    }
    csv_data.append(csv_row)

# Define CSV file path
csv_file_path = 'csv_file/CA_category_id.csv'

# Write data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['kind', 'etag', 'id', 'channelId', 'assignable', 'title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print(f"CSV file saved at: {csv_file_path}")

# Convert CSV to Excel
excel_file_path = 'csv_file/CA_category_id.xlsx'
df = pd.DataFrame(csv_data)
df.to_excel(excel_file_path, index=False)

print(f"Excel file saved at: {excel_file_path}")
