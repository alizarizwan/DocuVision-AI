import cv2
import pytesseract
import numpy as np

# Configure Tesseract OCR Path (Adjust based on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """Extracts text from an engineering document using Tesseract OCR."""
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding for better text detection
    processed_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(processed_img)

    return extracted_text.strip()

# Example Usage:
if __name__ == "__main__":
    text = extract_text("sample_document.png")
    print(text)
