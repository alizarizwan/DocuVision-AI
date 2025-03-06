from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient

# SQL Database Setup (PostgreSQL or SQLite)
SQL_DATABASE_URL = "sqlite:///./documents.db"
engine = create_engine(SQL_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    category = Column(String)

Base.metadata.create_all(bind=engine)

# NoSQL Database Setup (MongoDB)
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["document_analysis"]
mongo_collection = mongo_db["documents"]

def save_to_sql(text, category):
    """Saves extracted text and category into SQL database."""
    session = SessionLocal()
    doc = Document(text=text, category=category)
    session.add(doc)
    session.commit()

def save_to_nosql(text, category):
    """Saves extracted text and category into MongoDB."""
    doc = {"text": text, "category": category}
    mongo_collection.insert_one(doc)
