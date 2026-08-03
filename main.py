import cv2
import sys
import os
import glob

# 1. Properly check for CLI arguments
if len(sys.argv) < 2:
    if getattr(sys, 'frozen', False):
        print("usage: graphia <path/of/image_or_folder>")
    elif os.name == 'nt':
        print("usage: python main.py <path/of/image_or_folder>")
    else:
        print("usage: python3 main.py <path/of/image_or_folder>")
    sys.exit(1)

# Get argument as a string
input_path = sys.argv[1]

# 2. Determine base directory for the output folder
if os.path.isdir(input_path):
    base_dir = input_path
elif os.path.isfile(input_path):
    base_dir = os.path.dirname(input_path)
else:
    # Handles wildcard paths like "folder/*" or non-existent paths
    base_dir = os.path.dirname(input_path) or "."

output = os.path.join(base_dir, "graphia")

# Create output directory if it doesn't exist
if not os.path.exists(output):
    try:
        os.makedirs(output, exist_ok=True)
    except Exception as e:
        print(f"Failed to create directory: {e}")
        sys.exit(1)

def gray(source, output_dir=output):
    try:
        if os.path.isfile(source):
            img = cv2.imread(source, cv2.IMREAD_UNCHANGED)

            if img is None:
                print(f"Skipping (not a valid image or unsupported format): {source}")
                return None

            # Handle PNGs with alpha channels (4 channels) or single channel images
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

# 3. Handle processing for both single files and directory searches
if os.path.isfile(input_path):
    gray(input_path)
else:
    # Expand path if user passes "folder/*" or just "folder"
    search_path = input_path if "*" in input_path else os.path.join(input_path, "*")
    
    files = [f for f in glob.glob(search_path) if os.path.isfile(f)]
    if not files:
        print(f"No files found for path: {input_path}")
    else:
        for item in files:
            gray(item)