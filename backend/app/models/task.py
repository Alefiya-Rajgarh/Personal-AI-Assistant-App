from __future__ import annotations

import enum
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class TaskPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class TaskStatus(str, enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELLED = "CANCELLED"


class Task(BaseModel):
    __tablename__ = "tasks"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    due_date: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority, name="task_priority"),
        server_default=TaskPriority.MEDIUM.value,
    )
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status"),
        server_default=TaskStatus.TODO.value,
    )
    tags: Mapped[dict | None] = mapped_column(JSONB)
    related_meeting_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("meetings.id", ondelete="SET NULL"),
        index=True,
    )

    __table_args__ = (
        Index("ix_tasks_user_id", "user_id"),
        Index("ix_tasks_related_meeting_id", "related_meeting_id"),
    )
