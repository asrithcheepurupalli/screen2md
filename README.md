# screen2md

This is a simple tool I made to convert screenshots into `.md`, `.txt`, or `.pdf` notes using OCR. It lets me pull text from class notes, code images, or random screenshots and save them as clean files.

No fancy UI or anything — just drop images into the folder, run it, and you’re good.

---

## Features

- Converts `.png`, `.jpg`, `.jpeg` images into text
- Output formats:
  - Markdown (`.md`)
  - Plain text (`.txt`)
  - PDF (`.pdf`) with Unicode-safe font
- Works on multiple images at once
- Clean and human-readable output

---

## How to use

1. Put your screenshots inside the `screenshots/` folder  
2. Make sure `DejaVuSans.ttf` is inside the `fonts/` folder  
3. Run:

```bash
python main.py

 ---
 
# Requirements

Python 3.7+
Tesseract OCR
PIL (Pillow)
fpdf2
Install the Python packages:

pip install pytesseract pillow fpdf
Also make sure Tesseract is installed on your system.
On macOS:

brew install tesseract
Notes

PDF export needs fonts/DejaVuSans.ttf.
You can download it from the DejaVu GitHub
If you get weird OCR output, it’s probably the image quality
It skips lines that are too long or break layout, but most normal stuff works fine
Why I made this

Mostly for myself — I got tired of typing from screenshots or converting notes manually.
This does the job with minimum effort.

Author

Made by Lok Sai Asrith Cheepurupalli
asrithcheepurupalli.codes
GitHub