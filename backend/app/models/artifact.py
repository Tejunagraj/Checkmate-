import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    Boolean, DateTime, Float, ForeignKey,
    Integer, JSON, String, Text
)
from sqlalchemy.orm import Mapped, mapped_column

from app.persistence.base import Base


class ArtifactCard(Base):
    __tablename__ = "artifact_cards"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    session_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    summary: Mapped[str] = mapped_column(Text, default="", nullable=False)
    description: Mapped[str] = mapped_column(Text, default="", nullable=False)

    status: Mapped[str] = mapped_column(
        String(30), default="proposed", nullable=False
    )
    locked: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    risk_level: Mapped[str] = mapped_column(
        String(20), default="low", nullable=False
    )
    confidence: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )

    reasoning: Mapped[str] = mapped_column(Text, default="", nullable=False)
    evidence: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    assumptions: Mapped[list] = mapped_column(JSON, default=list, nullable=False)

    updated_by: Mapped[str] = mapped_column(
        String(50), default="agent", nullable=False
    )
    version: Mapped[int] = mapped_column(
        Integer, default=1, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )