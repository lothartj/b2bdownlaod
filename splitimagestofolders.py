import os
import shutil

# Define source and target directories
source_dir = r"C:\downloadb2bimages\B2B\images\main"
target_dir1 = r"C:\downloadb2bimages\B2B\images\folder1"
target_dir2 = r"C:\downloadb2bimages\B2B\images\folder2"

# Ensure target directories exist
os.makedirs(target_dir1, exist_ok=True)
os.makedirs(target_dir2, exist_ok=True)

# List all files in the source directory
all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# Verify there are exactly 1033 images
if len(all_files) != 1033:
    raise ValueError("The number of files is not exactly 1033.")

# Split the list of files
first_half_files = all_files[:517]
second_half_files = all_files[517:]

# Copy the first half to folder1
for file in first_half_files:
    shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir1, file))

# Copy the second half to folder2
for file in second_half_files:
    shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir2, file))

print("Files have been successfully copied.")
