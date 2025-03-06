import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

def clean_text(text):
    """Cleans extracted OCR text by removing special characters and stopwords."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words("english")]
    return " ".join(words)

def process_ocr_text(text):
    """Transforms extracted text into structured Pandas DataFrame."""
    cleaned_text = clean_text(text)
    df = pd.DataFrame({"Processed_Text": [cleaned_text]})
    return df

# Example Usage:
if __name__ == "__main__":
    sample_text = "This is a sample engineering drawing document with specifications."
    print(process_ocr_text(sample_text))
