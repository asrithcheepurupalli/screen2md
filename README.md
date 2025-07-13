# Screen2MD

A simple CLI tool that converts screenshots or images with text into editable Markdown, PDF, or plain text files using OCR.

## Features

- Extracts text from `.png`, `.jpg`, `.jpeg`, `.webp` images using Tesseract OCR.
- Supports Markdown, PDF, and TXT outputs.
- Automatically timestamps and names your notes.
- Lightweight and fully offline.
- Option to convert specific files from the folder or all at once.

## Folder Structure

```
screen2md/
├── images/          # Place your screenshots here
├── output/          # Converted files will be saved here
├── main.py          # Main CLI script
├── README.md
└── requirements.txt
```

## Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Also ensure Tesseract is installed on your system:

### macOS (Homebrew):
```
brew install tesseract
```

### Ubuntu/Debian:
```
sudo apt update
sudo apt install tesseract-ocr
```

### Windows:
Download from https://github.com/tesseract-ocr/tesseract

## Usage

```
python main.py
```

You'll be prompted to:
- Choose the image(s) to convert
- Select the output format (`md`, `txt`, or `pdf`)

Converted files will be saved to the `output/` folder.

## Why Use This?

Whether you're documenting debugging sessions, saving notes from screenshots, or digitizing printed text, Screen2MD helps you extract and store that content in a clean, readable, and organized way — without lifting a finger to type it out.

## Dependencies

- Python 3.8+
- pytesseract
- Pillow
- fpdf2

## Author

Lok Sai Asrith Cheepurupalli  
https://asrithcheepurupalli.codes
