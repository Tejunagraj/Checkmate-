import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.persistence.base import Base


class CollaborationSession(Base):
    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    goal: Mapped[str] = mapped_column(String(1000), nullable=False)
    scenario: Mapped[str] = mapped_column(
        String(100), default="custom", nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(30), default="active", nullable=False
    )
    constraints: Mapped[list] = mapped_column(
        JSON, default=list, nullable=False
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