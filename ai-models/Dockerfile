FROM python:3.14-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/model-cache

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch==2.14.1+cpu

RUN grep -v '^torch==' requirements.txt > requirements-docker.txt \
    && pip install --no-cache-dir -r requirements-docker.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
