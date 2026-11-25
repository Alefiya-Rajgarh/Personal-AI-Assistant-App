from __future__ import annotations

import enum
import uuid

from sqlalchemy import Enum, ForeignKey, Index, Integer, String, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class CommunicationStyle(str, enum.Enum):
    FORMAL = "FORMAL"
    CASUAL = "CASUAL"


class UserPreference(BaseModel):
    __tablename__ = "user_preferences"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    preferred_working_hours_start: Mapped[Time | None] = mapped_column(Time)
    preferred_working_hours_end: Mapped[Time | None] = mapped_column(Time)
    preferred_meeting_duration: Mapped[int | None] = mapped_column(Integer)
    commute_home_address: Mapped[str | None] = mapped_column(String(255))
    commute_work_address: Mapped[str | None] = mapped_column(String(255))
    communication_style: Mapped[CommunicationStyle | None] = mapped_column(
        Enum(CommunicationStyle, name="communication_style"),
    )
    notification_lead_time_minutes: Mapped[int | None] = mapped_column(Integer)
    preferred_travel_mode: Mapped[str | None] = mapped_column(String(64))

    __table_args__ = (Index("ix_user_preferences_user_id", "user_id"),)
