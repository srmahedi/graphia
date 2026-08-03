# Graphia

Graphia is a simple Python script that converts an image to grayscale using OpenCV.

## Features

- Converts color images to grayscale
- Preserves the original file extension
- Automatically creates an output folder named `graphia`
- Saves the converted image without modifying the original

## Requirements

- Python 3.x
- OpenCV

Install the required dependency:

```bash
pip install opencv-python
```

## Usage

### Windows

```bash
python main.py path\to\image.jpg
```

### Linux/macOS

```bash
python3 main.py /path/to/image.jpg
```

## Output

The script creates a folder named `graphia` in the same directory as the input image.

Example:

```
Images/
├── photo.jpg
└── graphia/
    └── photo-gray.jpg
```

After processing, the script prints the output path:

```
Output: C:\Images\graphia\photo-gray.jpg
```

## Project Structure

```
.
├── main.py
└── README.md
```

## Error Handling

The script will report an error if:

- No image path is provided.
- The image cannot be read.
- The output directory cannot be created.
- An unexpected error occurs during processing.

## Example

Input:

```
photo.png
```

Command:

```bash
python main.py photo.png
```

Output:

```
graphia/photo-gray.png
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
