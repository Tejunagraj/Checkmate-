
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.persistence.database import engine
from app.persistence.base import Base

# Import models so SQLAlchemy registers their tables
from app import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initial development setup.
    # We will introduce formal migrations as the schema grows.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="CHECKMATE API",
    description="Checkpoint-Based Human-Agent Collaboration Platform",
    version="1.0.0",
    lifespan=lifespan
)

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


@app.get("/api/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "database": "connected",
            "type": "SQLite"
        }

    except Exception:
        return {
            "status": "error",
            "database": "disconnected"
        }
