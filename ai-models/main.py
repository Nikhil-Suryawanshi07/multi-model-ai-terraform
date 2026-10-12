from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from sentence_transformers import SentenceTransformer

app = FastAPI(
    title="Multi-Model AI Deployment",
    description="Sentiment Analysis and Text Embeddings API on AWS EC2",
    version="2.0.0"
)

# Model 1: Sentiment Analysis
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=-1
)

# Model 2: Text Embeddings
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device="cpu"
)

class PredictionRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Multi-Model AI API is running!",
        "models": ["DistilBERT Sentiment Analysis", "MiniLM Text Embeddings"]
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "sentiment_model_loaded": True,
        "embedding_model_loaded": True
    }

@app.post("/predict")
def predict(request: PredictionRequest):
    result = sentiment_model(request.text)[0]
    return {
        "input_text": request.text,
        "label": result["label"],
        "confidence": round(result["score"], 4)
    }

@app.post("/embeddings")
def embeddings(request: PredictionRequest):
    vector = embedding_model.encode(
        request.text,
        normalize_embeddings=True
    ).tolist()

    return {
        "input_text": request.text,
        "model": "all-MiniLM-L6-v2",
        "dimensions": len(vector),
        "embedding": vector
    }
