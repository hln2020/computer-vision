import os
import argparse

def rename_files(root_directory):
    # Walk through all subdirectories in the given root directory
    for subdir, dirs, files in os.walk(root_directory):
        for file in files:
            # Check if the filename matches the 'image_?.png' pattern
            if file.startswith("image_") and file.endswith(".png") and len(file) == 11:
                old_path = os.path.join(subdir, file)
                # Extract the digit from the filename
                digit = file[6:-4]
                # Check if the digit is a single character
                if digit.isdigit() and len(digit) == 1:
                    # Form the new filename with a leading zero
                    new_filename = f"image_0{digit}.png"
                    print(new_filename)
                    new_path = os.path.join(subdir, new_filename)
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Rename files in specified directory")
parser.add_argument('--dir', type=str, required=True, help='Specify the root directory for file renaming')

# Parse arguments from the command line
args = parser.parse_args()

# Example usage with command line argument
rename_files(args.dir)