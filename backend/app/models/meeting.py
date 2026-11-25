from __future__ import annotations

import enum
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class MeetingStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    RESCHEDULED = "RESCHEDULED"
    COMPLETED = "COMPLETED"


class Meeting(BaseModel):
    __tablename__ = "meetings"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    google_event_id: Mapped[str | None] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    start_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    location: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[MeetingStatus] = mapped_column(
        Enum(MeetingStatus, name="meeting_status"),
        server_default=MeetingStatus.SCHEDULED.value,
    )
    attendees: Mapped[dict | None] = mapped_column(JSONB)
    meeting_link: Mapped[str | None] = mapped_column(String(500))
    recurrence_rule: Mapped[str | None] = mapped_column(String(500))
    timezone: Mapped[str | None] = mapped_column(String(64))

    __table_args__ = (
        Index("ix_meetings_user_id", "user_id"),
        Index("ix_meetings_user_start", "user_id", "start_time"),
    )
