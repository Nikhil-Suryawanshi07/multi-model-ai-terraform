from fastapi import FastAPI, UploadFile, File, HTTPException
from transformers import pipeline
from PIL import Image
import io

app = FastAPI(
    title="AI Image Classification API",
    description="MobileNetV2 image classification on AWS EC2",
    version="1.0.0"
)

image_model = pipeline(
    "image-classification",
    model="google/mobilenet_v2_1.0_224",
    device=-1
)

@app.get("/health")
def health():
    return {"status": "ok", "image_model_loaded": True}

@app.post("/classify-image")
async def classify_image(file: UploadFile = File(...)):
    if file.content_type not in ("image/jpeg", "image/png", "image/webp"):
        raise HTTPException(
            status_code=415,
            detail="Upload a JPEG, PNG, or WebP image."
        )

    try:
        contents = await file.read()
        if len(contents) > 10 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="Image must be 10 MB or smaller.")

        image = Image.open(io.BytesIO(contents)).convert("RGB")
        predictions = image_model(image, top_k=3)

        return {
            "model": "MobileNetV2",
            "predictions": [
                {
                    "label": item["label"],
                    "confidence": round(item["score"], 4)
                }
                for item in predictions
            ]
        }
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=400, detail="Could not process this image.")
