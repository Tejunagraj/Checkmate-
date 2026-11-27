
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

# Database configuration
from app.persistence.database import engine
from app.persistence.base import Base

# Import models to register database tables
from app import models

# Import API routers
from app.api.sessions import router as sessions_router


# ==========================================
# DATABASE LIFECYCLE
# ==========================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize database tables when the application starts.
    """
    Base.metadata.create_all(bind=engine)

    yield

    # Application shutdown handling can be added here.


# ==========================================
# FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="CHECKMATE API",
    description=(
        "Checkpoint-Based Human-Agent "
        "Collaboration Platform"
    ),
    version="1.0.0",
    lifespan=lifespan
)


# ==========================================
# CORS CONFIGURATION
# ==========================================

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


# ==========================================
# API ROUTER REGISTRATION
# ==========================================

app.include_router(sessions_router)


# ==========================================
# ROOT ENDPOINT
# ==========================================

@app.get("/")
def root():
    return {
        "project": "CHECKMATE",
        "message": "Welcome to CHECKMATE API",
        "status": "running"
    }


# ==========================================
# BACKEND HEALTH CHECK
# ==========================================

@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "project": "CHECKMATE",
        "backend": "running",
        "message": "CHECKMATE backend is ready"
    }


# ==========================================
# DATABASE HEALTH CHECK
# ==========================================

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
