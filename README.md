# Graphia

Graphia is a lightweight Python utility that converts images to grayscale using OpenCV. It can process a single image or every file inside a directory, while preserving the original image format.

## Features

* Convert a single image to grayscale.
* Batch process all files in a directory.
* Preserves the original file extension.
* Supports common image formats supported by OpenCV.
* Handles images with RGB, RGBA, and grayscale channels.
* Automatically creates a `graphia` output directory.
* Leaves the original files unchanged.
* Prints the output path for every successfully processed image.

## Requirements

* Python 3.x
* OpenCV

Install the required dependency:

```bash
pip install opencv-python
```

## Usage

### Windows

```bash
python main.py <path/to/image_or_folder>
```

Example:

```bash
python main.py image.jpg
python main.py C:\Images
```

### Linux/macOS

```bash
python3 main.py <path/to/image_or_folder>
```

Example:

```bash
python3 main.py image.jpg
python3 main.py /home/user/Pictures
```

If Graphia is distributed as a standalone executable:

```bash
graphia <path/to/image_or_folder>
```

## Output

Graphia creates a directory named `graphia` inside the input image's directory or inside the processed folder.

### Processing a Single Image

```
Images/
├── photo.jpg
└── graphia/
    └── photo-gray.jpg
```

### Processing a Folder

```
Images/
├── photo1.jpg
├── photo2.png
├── photo3.bmp
└── graphia/
    ├── photo1-gray.jpg
    ├── photo2-gray.png
    └── photo3-gray.bmp
```

For every successfully processed image, Graphia prints:

```
Output: /path/to/graphia/photo-gray.jpg
```

## Supported Input

* Single image file

```bash
python main.py photo.png
```

* Directory

```bash
python main.py Pictures
```

* Wildcard path

```bash
python main.py Pictures/*
```

## Project Structure

```
.
├── main.py
└── README.md
```

## Error Handling

Graphia reports appropriate messages when:

* No input path is provided.
* The specified path contains no files.
* An image cannot be read or is not a supported format.
* The output directory cannot be created.
* An unexpected processing error occurs.

Invalid or unsupported files are skipped without stopping the remaining processing.

## Example

Input directory:

```
Pictures/
├── cat.jpg
├── dog.png
└── logo.png
```

Command:

```bash
python main.py Pictures
```

Output:

```
Output: Pictures/graphia/cat-gray.jpg
Output: Pictures/graphia/dog-gray.png
Output: Pictures/graphia/logo-gray.png
```

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.
