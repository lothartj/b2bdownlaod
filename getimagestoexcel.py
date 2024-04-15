import os
from openpyxl import Workbook

# Function to get all image files in a directory
def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_files.append(filename)
    return image_files

# Path to the directory containing images
image_directory = r'C:\downloadb2bimages\images'

# Get all image files from the directory
image_files = get_image_files(image_directory)

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Add column headers
sheet['A1'] = 'Image Name'

# Iterate through image files, remove the "-1.jpg" suffix, and insert their names into the Excel sheet
for idx, image_file in enumerate(image_files, start=2):  # Start from row 2 to avoid overwriting headers
    image_name = os.path.splitext(image_file)[0]  # Remove file extension
    image_name = image_name.replace('-1', '')     # Remove "-1" suffix
    image_name = f'"{image_name}",'               # Add double quotes around the name and comma at the end
    sheet[f'A{idx}'] = image_name

# Save the workbook in the specified folder
excel_file_path = r'C:\downloadb2bimages\images.xlsx'
workbook.save(excel_file_path)
