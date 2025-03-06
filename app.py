from fastapi import FastAPI, UploadFile, File
import shutil
from ocr import extract_text
from preprocess import process_ocr_text
from model import predict_text_class
from database import save_to_sql, save_to_nosql

app = FastAPI()

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    """Uploads a document, extracts text, processes it, classifies it, and stores it."""
    file_path = f"temp_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR Extraction
    extracted_text = extract_text(file_path)
    
    # Text Processing
    processed_df = process_ocr_text(extracted_text)
    processed_text = processed_df["Processed_Text"][0]

    # Classification
    category = predict_text_class(processed_text)

    # Save to Databases
    save_to_sql(processed_text, category)
    save_to_nosql(processed_text, category)

    return {"extracted_text": extracted_text, "category": category}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
