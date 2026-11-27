import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    DateTime, ForeignKey, Integer, JSON, String, Text
)
from sqlalchemy.orm import Mapped, mapped_column

from app.persistence.base import Base


class Checkpoint(Base):
    __tablename__ = "checkpoints"

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

    sequence_number: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(
        String(30), default="pending", nullable=False
    )
    steering_note: Mapped[str] = mapped_column(
        Text, default="", nullable=False
    )
    proposed_changes: Mapped[list] = mapped_column(
        JSON, default=list, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )