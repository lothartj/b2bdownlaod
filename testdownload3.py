
import os
import shutil
from pygoogle_image import image as pi


# Specify the desired folder path
folder_path = 'C:\\downloadb2bimages\\itemimages\\image3'
os.makedirs(folder_path, exist_ok=True)

descriptions =  [



]

# Specify the desired size for the new image
desired_size = (300, 300)  # Adjust the size as needed

for description in descriptions:
    # Change the current working directory to the desired folder
    os.chdir(folder_path)

    # Download images without specifying output_directory
    pi.download(description, limit=10)
    # Change back to the original working directory
    os.chdir("..")
    print(description, 'downloaded successfully')
