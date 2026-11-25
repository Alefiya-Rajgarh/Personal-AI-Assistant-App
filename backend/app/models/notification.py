from __future__ import annotations

import enum
import uuid

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class NotificationType(str, enum.Enum):
    MEETING_REMINDER = "MEETING_REMINDER"
    DEPARTURE_ALERT = "DEPARTURE_ALERT"
    EMAIL_RECEIVED = "EMAIL_RECEIVED"
    TASK_DUE = "TASK_DUE"
    SYSTEM = "SYSTEM"


class Notification(BaseModel):
    __tablename__ = "notifications"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    type: Mapped[NotificationType] = mapped_column(
        Enum(NotificationType, name="notification_type"),
    )
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    data: Mapped[dict | None] = mapped_column(JSONB)
    is_read: Mapped[bool] = mapped_column(Boolean, server_default="false")
    scheduled_for: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    sent_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))

    __table_args__ = (Index("ix_notifications_user_id", "user_id"),)
