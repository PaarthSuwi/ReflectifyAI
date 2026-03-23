from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Gemini handles summarization.

app = FastAPI()

# Allow frontend origin (adjust if deployed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Record(BaseModel):
    title: str
    content: str

class SummaryRequest(BaseModel):
    content: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Reflectify.ai API"}

@app.post("/add-record")
def add_record(record: Record):
    return {"status": "success", "data": record}

# Summarization endpoint removed from here, exists in routers/ai.py
