from __future__ import annotations

import enum
import uuid

from sqlalchemy import Enum, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class DevicePlatform(str, enum.Enum):
    IOS = "IOS"
    ANDROID = "ANDROID"
    WEB = "WEB"


class DeviceToken(BaseModel):
    __tablename__ = "device_tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    platform: Mapped[DevicePlatform] = mapped_column(
        Enum(DevicePlatform, name="device_platform"),
    )
    token: Mapped[str] = mapped_column(String(512), unique=True)

    __table_args__ = (
        Index("ix_device_tokens_user_id", "user_id"),
        Index("ix_device_tokens_token", "token"),
    )
