# app.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

# Initialize the FastAPI app
app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DB_PATH = "insightstream.db"

# Ensure the database file exists
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE SentimentAnalysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        sentiment_score REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    cursor.execute('''
    CREATE TABLE TrendData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        positive_count INTEGER NOT NULL,
        negative_count INTEGER NOT NULL,
        neutral_count INTEGER NOT NULL
    )
    ''')
    # Insert mock data
    cursor.execute("INSERT INTO SentimentAnalysis (text, sentiment_score) VALUES (?, ?)", ("I love this product!", 0.9))
    cursor.execute("INSERT INTO TrendData (date, positive_count, negative_count, neutral_count) VALUES (?, ?, ?, ?)", ("2023-10-01", 10, 2, 5))
    conn.commit()
    conn.close()

# Models
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    id: int
    text: str
    sentiment_score: float
    timestamp: datetime

class TrendResponse(BaseModel):
    id: int
    date: str
    positive_count: int
    negative_count: int
    neutral_count: int

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard():
    return templates.TemplateResponse("dashboard.html", {"request": {}})

@app.get("/api-docs", response_class=HTMLResponse)
async def read_api_docs():
    return templates.TemplateResponse("api_docs.html", {"request": {}})

@app.get("/about", response_class=HTMLResponse)
async def read_about():
    return templates.TemplateResponse("about.html", {"request": {}})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact():
    return templates.TemplateResponse("contact.html", {"request": {}})

@app.get("/api/sentiment", response_model=List[SentimentResponse])
async def get_sentiments():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SentimentAnalysis")
    rows = cursor.fetchall()
    conn.close()
    return [SentimentResponse(id=row[0], text=row[1], sentiment_score=row[2], timestamp=row[3]) for row in rows]

@app.get("/api/trends", response_model=List[TrendResponse])
async def get_trends():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TrendData")
    rows = cursor.fetchall()
    conn.close()
    return [TrendResponse(id=row[0], date=row[1], positive_count=row[2], negative_count=row[3], neutral_count=row[4]) for row in rows]

@app.post("/api/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    # Mock sentiment analysis
    sentiment_score = 0.5 if "neutral" in request.text else 0.9 if "love" in request.text else 0.1
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SentimentAnalysis (text, sentiment_score) VALUES (?, ?)", (request.text, sentiment_score))
    conn.commit()
    sentiment_id = cursor.lastrowid
    cursor.execute("SELECT * FROM SentimentAnalysis WHERE id = ?", (sentiment_id,))
    row = cursor.fetchone()
    conn.close()
    return SentimentResponse(id=row[0], text=row[1], sentiment_score=row[2], timestamp=row[3])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
