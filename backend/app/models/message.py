from __future__ import annotations

import enum
import uuid

from sqlalchemy import Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class MessageRole(str, enum.Enum):
    USER = "USER"
    ASSISTANT = "ASSISTANT"
    TOOL = "TOOL"


class Message(BaseModel):
    __tablename__ = "messages"

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("conversation_sessions.id", ondelete="CASCADE"),
        index=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    role: Mapped[MessageRole] = mapped_column(
        Enum(MessageRole, name="message_role"),
    )
    content: Mapped[str] = mapped_column(Text)
    token_count: Mapped[int | None] = mapped_column(Integer)
    model_used: Mapped[str | None] = mapped_column(String(128))

    __table_args__ = (
        Index("ix_messages_session_id", "session_id"),
        Index("ix_messages_user_id", "user_id"),
    )
