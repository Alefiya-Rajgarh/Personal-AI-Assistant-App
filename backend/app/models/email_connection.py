from __future__ import annotations

import uuid

from sqlalchemy import Boolean, DateTime, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class EmailConnection(BaseModel):
    __tablename__ = "email_connections"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    provider: Mapped[str] = mapped_column(String(32), server_default="GMAIL")
    access_token: Mapped[str] = mapped_column(String(2048))
    refresh_token: Mapped[str | None] = mapped_column(String(2048))
    token_expiry: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
    scopes: Mapped[dict | None] = mapped_column(JSONB)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="true")

    __table_args__ = (Index("ix_email_connections_user_id", "user_id"),)
