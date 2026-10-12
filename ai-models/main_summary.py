
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = FastAPI(
    title="AI Text Summarization API",
    description="FLAN-T5-small summarization on AWS EC2",
    version="1.0.0"
)

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.eval()


class SummaryRequest(BaseModel):
    text: str = Field(min_length=20, max_length=5000)


@app.get("/")
def home():
    return {
        "message": "AI Text Summarization API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "summary_model_loaded": True
    }


@app.post("/summarize")
def summarize(request: SummaryRequest):
    prompt = (
        "Summarize the following text briefly:\n"
        + request.text
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=120,
            do_sample=False
        )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "model": "FLAN-T5-small",
        "summary": summary
    }
