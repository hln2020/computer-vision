import os
import argparse
from PIL import Image

def ensure_directory_exists(directory):
    """Create the directory if it does not exist."""
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory ensured: {directory}")
    except Exception as e:
        print(f"Failed to create directory {directory}: {e}")

def resize_and_save_image(file_path, dest_path):
    """Resize an image and save it to the specified path."""
    try:
        with Image.open(file_path) as img:
            img_resized = img.resize((240, 160), Image.LANCZOS)  # LANCZOS filter for high-quality downsampling
            img_resized.save(dest_path)
            print(f"Saved resized image to {dest_path}")
    except IOError as e:
        print(f"Error opening or processing image {file_path}: {e}")

def process_images(source_dir, destination_dir):
    """Process images from source directory and save them to destination directory."""
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if 'frame0022' in file and file.endswith('.png'):
                file_path = os.path.join(root, file)
                dest_path = os.path.join(destination_dir, file)
                resize_and_save_image(file_path, dest_path)

def main():
    parser = argparse.ArgumentParser(description='Resize PNG images in a specific frame.')
    parser.add_argument('--source_dir', type=str, required=True, help='The source directory where to look for PNG files')
    parser.add_argument('--destination_dir', type=str, default='./22nd', help='The destination directory where resized images will be saved')
    
    args = parser.parse_args()

    # Ensure the destination directory exists
    ensure_directory_exists(args.destination_dir)

    # Process images
    process_images(args.source_dir, args.destination_dir)

    print("Resizing completed.")

if __name__ == '__main__':
    main()
