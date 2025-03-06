# DocuVision-AI

# 📄 DocuVision AI - Automated Document Analysis with AI
# AI-powered OCR and classification system for engineering documents

# 🌟 Overview
# DocuVision AI is a machine learning-based document analysis tool that automates text extraction, classification, and storage from engineering documents using OCR, NLP, and AI models.

#🔹 Key Features:
# ✔ OCR Processing – Extracts text from scanned engineering drawings & documents
# ✔ Machine Learning Classification – Categorizes documents using AI
# ✔ SQL & NoSQL Database Storage – Stores extracted text & metadata for analysis
# ✔ REST API Integration – Provides a seamless interface for frontend & backend interaction
# ✔ User-friendly Web Interface – Upload & analyze documents via a modern UI

# 🚀 Tech Stack
# Backend: FastAPI, Python (OpenCV, Tesseract, TensorFlow/PyTorch, Pandas)
# Frontend: HTML, CSS, JavaScript (Fetch API)
# Database: SQLite (SQL), MongoDB (NoSQL)
# Machine Learning: NLP, LSTM (TensorFlow)

# 📌 Project Structure
# DocuVisionAI/
# │── backend/
# │   │── app.py               # FastAPI RESTful API
# │   │── ocr.py               # OCR text extraction (Tesseract, OpenCV)
# │   │── preprocess.py        # Text preprocessing (NLP, Pandas)
# │   │── model.py             # Text classification (TensorFlow)
# │   │── database.py          # SQL & NoSQL database management
# │── frontend/
# │   │── index.html           # Web UI
# │   │── script.js            # API Calls
# │   │── style.css            # Styling
# │── requirements.txt         # Dependencies
# │── README.md               # Documentation

# 🔧 Installation & Setup
# 1️⃣ Clone the Repository
# git clone https://github.com/yourusername/DocuVisionAI.git
# cd DocuVisionAI

# 2️⃣ Install Dependencies
# pip install -r requirements.txt

# 3️⃣ Start the Backend Server
# cd backend
# uvicorn app:app --reload

# 4️⃣ Start the Frontend
# Open frontend/index.html in your browser.
# Upload an engineering document & see the results!

