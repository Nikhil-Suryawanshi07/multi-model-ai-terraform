# Multi-Model AI Deployment on AWS EC2

Deploy multiple pretrained AI models as independent REST APIs using FastAPI, Docker, and AWS EC2.

## AI Models

| Model | Purpose | Port |
|---|---|---:|
| DistilBERT | Sentiment Analysis | 8000 |
| MiniLM | Sentence Embeddings | 8001 |
| MobileNetV2 | Image Classification | 8002 |
| FLAN-T5-small | Text Summarization | 8003 |

## Tech Stack

- AWS EC2
- Docker
- FastAPI
- Python
- Hugging Face Transformers
- Terraform

## Project Structure

- `ai-models/` — AI application code and Dockerfiles
- `main.tf` — Terraform infrastructure configuration
- `variables.tf` — Terraform variables
- `outputs.tf` — Terraform outputs
- `Jenkinsfile` — CI/CD pipeline configuration

## API Endpoints

- Port 8000: `/health`, `/predict`
- Port 8001: `/health`, `/predict`, `/embeddings`
- Port 8002: `/health`, `/classify-image`
- Port 8003: `/health`, `/summarize`

Open `/docs` on the relevant API port to explore and test endpoints.

## Deployment

Each AI model runs in a separate Docker container on AWS EC2. Terraform configuration is maintained for infrastructure provisioning.

## Security Notes

- Never commit AWS credentials, private keys, or secrets.
- Keep Terraform state files out of Git.
- Restrict API access to trusted IP addresses.
- Configure HTTPS before production use.
- Monitor AWS resource usage and costs.

## Project Status

Four AI model APIs have been deployed and tested on EC2. Automated CI/CD is not currently confirmed.

This project is intended for learning and demonstration purposes.
