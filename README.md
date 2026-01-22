# 🏦 Bank Note Authentication API

FastAPI application for predicting bank note authenticity using Machine Learning.

## 🚀 Quick Start

### Run Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python -m uvicorn app:app --reload
```

### Run with Docker
```bash
# Build image
docker build -t banknote-api .

# Run container
docker run -d -p 8000:8000 --name banknote-api banknote-api
```

## 📁 Project Structure
```
├── app.py              # Main FastAPI application
├── BankNotes.py        # Pydantic schema for request body
├── classifier.pkl      # Trained ML model
├── train_model.py      # Script to retrain model
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose config
└── data/
    └── BankNote_Authentication.csv  # Training data
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/{name}` | Welcome message |
| POST | `/predict` | Predict bank note authenticity |

## 📝 Example Request

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"variance": 2.5, "skewness": 3.2, "curtosis": 1.1, "entropy": -0.5}'
```

## 📦 Deploy to Railway

1. Push to GitHub
2. Connect repo to [Railway](https://railway.app)
3. Railway auto-detects Dockerfile and deploys

## ⚙️ Tech Stack

- **FastAPI** - Web framework
- **Scikit-learn** - ML model (Random Forest)
- **Docker** - Containerization
- **Uvicorn** - ASGI server