from __future__ import annotations

import uuid

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class TravelPlan(BaseModel):
    __tablename__ = "travel_plans"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    origin: Mapped[str] = mapped_column(String(255))
    destination: Mapped[str] = mapped_column(String(255))
    departure_time: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    arrival_time: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    travel_mode: Mapped[str | None] = mapped_column(String(64))
    distance_meters: Mapped[int | None] = mapped_column(Integer)
    duration_seconds: Mapped[int | None] = mapped_column(Integer)
    traffic_duration_seconds: Mapped[int | None] = mapped_column(Integer)
    route_polyline: Mapped[str | None] = mapped_column(String(2048))
    related_meeting_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("meetings.id", ondelete="SET NULL"),
        index=True,
    )

    __table_args__ = (
        Index("ix_travel_plans_user_id", "user_id"),
        Index("ix_travel_plans_related_meeting_id", "related_meeting_id"),
    )
