import re
import hashlib

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def compute_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
