from pypdf import PdfReader
import re

def clean_text(text: str) -> str:
    text = re.sub(
        r'(?:(?<=\b)[A-Za-z]\s)+(?:[A-Za-z])',
        lambda m: m.group(0).replace(" ", ""),
        text
    )
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    raw_text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            raw_text += page_text + " "

    return clean_text(raw_text)
