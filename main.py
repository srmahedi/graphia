import cv2
import sys
import os
import glob

# 1. Check CLI arguments
if len(sys.argv) < 2:
    if getattr(sys, 'frozen', False):
        print("usage: graphia <path/of/image_or_folder>")
    elif os.name == 'nt':
        print("usage: python main.py <path/of/image_or_folder>")
    else:
        print("usage: python3 main.py <path/of/image_or_folder>")
    sys.exit(1)

def get_output_dir(source_path):
    """Determines output directory based on input path type."""
    if os.path.isdir(source_path):
        base_dir = source_path
    else:
        base_dir = os.path.dirname(source_path) or "."

    output_dir = os.path.join(base_dir, "graphia")
    
    # Create the directory safely
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Failed to create directory {output_dir}: {e}")
        return None
        
    return output_dir

def gray(source, output_dir):
    """Converts a single image to grayscale."""
    if not output_dir:
        return None

    try:
        if not os.path.isfile(source):
            return None

        img = cv2.imread(source, cv2.IMREAD_UNCHANGED)

        if img is None:
            print(f"Skipping (not a valid image or unsupported format): {source}")
            return None

        # Handle PNGs with alpha channels (4 channels) or 3-channel images
        if len(img.shape) == 3 and img.shape[2] == 4:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        elif len(img.shape) == 3 and img.shape[2] == 3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = img  # Already single-channel

        get_name = os.path.basename(source)
        file_name, file_ext = os.path.splitext(get_name)
        output_file = os.path.join(output_dir, f"{file_name}-gray{file_ext}")

        cv2.imwrite(output_file, gray_img)
        print(f"Output: {output_file}")
        return output_file
    except Exception as e:
        print(f"Error processing {source}: {e}")

# 2. Iterate through all items passed via sys.argv[1:]
inputs = sys.argv[1:]

for input_path in inputs:
    output_directory = get_output_dir(input_path)

    # Case 1: Single file (e.g., 'Desktop/New Folder/988943.jpg' or expanded wildcards)
    if os.path.isfile(input_path):
        gray(input_path, output_dir=output_directory)

    # Case 2: Directory passed directly (e.g., 'Desktop/New Folder/')
    elif os.path.isdir(input_path):
        search_path = os.path.join(input_path, "*")
        files = [f for f in glob.glob(search_path) if os.path.isfile(f)]
        if not files:
            print(f"No files found in directory: {input_path}")
        else:
            for item in files:
                gray(item, output_dir=output_directory)

    # Case 3: Quoted wildcards (e.g., "folder/*" or '*')
    elif "*" in input_path:
        files = [f for f in glob.glob(input_path) if os.path.isfile(f)]
        if not files:
            print(f"No files matched pattern: {input_path}")
        else:
            for item in files:
                gray(item, output_dir=output_directory)

    # Case 4: Non-existent file/path
    else:
        print(f"Skipping invalid or missing path: {input_path}")