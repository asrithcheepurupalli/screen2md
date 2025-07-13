import os
from datetime import datetime
from PIL import Image
import pytesseract
from fpdf import FPDF
import unicodedata

INPUT_DIR = "screenshots"
OUTPUT_DIR = "notes"
FONT_PATH = os.path.join("fonts", "DejaVuSans.ttf")

def clean_text(text):
    return unicodedata.normalize("NFKC", text).replace("\u00A0", " ")

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        print("Error reading", image_path, ":", e)
        return ""

def save_text_file(text, name, ts):
    path = os.path.join(OUTPUT_DIR, f"{ts}_{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip())
    return path

def save_markdown(text, name, ts):
    path = os.path.join(OUTPUT_DIR, f"{ts}_{name}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Notes\n\n" + text.strip())
    return path

def save_pdf(text, name, ts):
    path = os.path.join(OUTPUT_DIR, f"{ts}_{name}.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    if not os.path.exists(FONT_PATH):
        print("Font not found:", FONT_PATH)
        return None

    pdf.add_font("DejaVu", "", FONT_PATH)
    pdf.set_font("DejaVu", size=10)

    for line in clean_text(text).splitlines():
        try:
            line = line.replace("\t", "    ").strip()
            if not line:
                pdf.ln(7)
                continue
            while len(line) > 100:
                pdf.multi_cell(0, 7, line[:100])
                line = line[100:]
            pdf.multi_cell(0, 7, line)
        except Exception as e:
            print("Skipped a line due to PDF error:", e)

    pdf.output(path)
    return path

def save_file(text, name, fmt):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
    base = name.rsplit(".", 1)[0].replace(" ", "_")
    if fmt == "txt":
        return save_text_file(text, base, ts)
    elif fmt == "md":
        return save_markdown(text, base, ts)
    elif fmt == "pdf":
        return save_pdf(text, base, ts)
    else:
        print("Unknown format:", fmt)
        return None

def list_images():
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    for i, f in enumerate(files):
        print(f"[{i+1}] {f}")
    return files

def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = list_images()
    if not files:
        print("No images found in", INPUT_DIR)
        return

    selected = input("Enter image numbers to convert (e.g. 1 3): ").split()
    try:
        images = [files[int(i)-1] for i in selected]
    except:
        print("Invalid selection.")
        return

    fmt = input("Choose output format (txt/md/pdf): ").strip().lower()
    for img in images:
        text = extract_text(os.path.join(INPUT_DIR, img))
        if not text.strip():
            print("No text found in", img)
            continue
        out = save_file(text, img, fmt)
        if out:
            print("Saved →", out)

if __name__ == "__main__":
    main()
