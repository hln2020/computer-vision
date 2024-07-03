import os
import shutil

def duplicate_files(root_folder):
    # Walk through all directories and files in the root folder
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            # Construct the full path to the current file
            original_file_path = os.path.join(dirpath, filename)
            # Construct the path for the duplicated file
            duplicated_file_path = os.path.join(dirpath, f"z_{filename}")
            # Copy the original file to the new location with the new name
            shutil.copy2(original_file_path, duplicated_file_path)
            print(f"Duplicated: {original_file_path} to {duplicated_file_path}")

# Specify the root directory to start duplication
root_directory = './hidden'
duplicate_files(root_directory)