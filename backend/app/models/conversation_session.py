from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class ConversationSession(BaseModel):
    __tablename__ = "conversation_sessions"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str | None] = mapped_column(String(255))

    __table_args__ = (Index("ix_conversation_sessions_user_id", "user_id"),)
