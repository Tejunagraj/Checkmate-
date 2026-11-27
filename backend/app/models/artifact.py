import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, JSON, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.persistence.base import Base

class ArtifactCard(Base):
    __tablename__ = "artifact_cards"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id: Mapped[str] = mapped_column(ForeignKey("sessions.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    summary: Mapped[str] = mapped_column(String(1000), default="")
    description: Mapped[str] = mapped_column(String, default="")
    status: Mapped[str] = mapped_column(String(30), default="proposed")
    locked: Mapped[bool] = mapped_column(Boolean, default=False)
    risk_level: Mapped[str] = mapped_column(String(30), default="low")
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    reasoning: Mapped[str] = mapped_column(String, default="")
    evidence: Mapped[list] = mapped_column(JSON, default=list)
    assumptions: Mapped[list] = mapped_column(JSON, default=list)
    updated_by: Mapped[str] = mapped_column(String(100), default="system")
    version: Mapped[int] = mapped_column(Integer, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
