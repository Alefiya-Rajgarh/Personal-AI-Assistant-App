from __future__ import annotations

import enum
import uuid

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, Enum, Float, ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class MemoryType(str, enum.Enum):
    PREFERENCE = "PREFERENCE"
    FACT = "FACT"
    PATTERN = "PATTERN"
    EVENT = "EVENT"


class AgentMemory(BaseModel):
    __tablename__ = "agent_memories"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    memory_type: Mapped[MemoryType] = mapped_column(
        Enum(MemoryType, name="memory_type"),
    )
    content: Mapped[str] = mapped_column(Text)
    embedding: Mapped[list[float]] = mapped_column(Vector(1536))
    metadata_: Mapped[dict | None] = mapped_column("metadata", JSONB)
    importance_score: Mapped[float | None] = mapped_column(Float)
    last_accessed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        Index("ix_agent_memories_user_id", "user_id"),
        Index(
            "ix_agent_memories_embedding",
            "embedding",
            postgresql_using="ivfflat",
            postgresql_ops={"embedding": "vector_cosine_ops"},
        ),
    )
