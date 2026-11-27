
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CHECKMATE API",
    description="Checkpoint-Based Human-Agent Collaboration Platform",
    version="1.0.0"
)

# Allow the Ember.js frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "project": "CHECKMATE",
        "message": "Welcome to CHECKMATE API",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "project": "CHECKMATE",
        "backend": "running",
        "message": "CHECKMATE backend is ready"
    }
