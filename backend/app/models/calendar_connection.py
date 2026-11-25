from __future__ import annotations

import enum
import uuid

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class CalendarProvider(str, enum.Enum):
    GOOGLE = "GOOGLE"
    OUTLOOK = "OUTLOOK"


class CalendarConnection(BaseModel):
    __tablename__ = "calendar_connections"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    provider: Mapped[CalendarProvider] = mapped_column(
        Enum(CalendarProvider, name="calendar_provider"),
    )
    access_token: Mapped[str] = mapped_column(String(2048))
    refresh_token: Mapped[str | None] = mapped_column(String(2048))
    token_expiry: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    calendar_id: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="true")

    __table_args__ = (Index("ix_calendar_connections_user_id", "user_id"),)
