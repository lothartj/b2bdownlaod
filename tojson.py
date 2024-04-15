# items.py
import pandas as pd
import json

# Load the Excel file
excel_path = r'C:\downloadb2bimages\Items (81).xlsx'
df = pd.read_excel(excel_path)

# Print column names
print("Column Names:", df.columns)

# Create a list of dictionaries
item_list = [{row['No.']: row['Description']} for _, row in df.iterrows()]

# Save the list of dictionaries to a JSON file
json_file_path = r'C:\downloadb2bimages\item_list.json'
with open(json_file_path, 'w') as json_file:
    json.dump(item_list, json_file)

print(f'JSON file saved at: {json_file_path}')
