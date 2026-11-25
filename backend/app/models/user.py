from __future__ import annotations

import enum

from sqlalchemy import Boolean, Enum, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class UserRole(str, enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    SUPER_ADMIN = "SUPER_ADMIN"


class User(BaseModel):
    __tablename__ = "users"

    firebase_uid: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str | None] = mapped_column(String(255))
    avatar_url: Mapped[str | None] = mapped_column(String(500))
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        server_default=UserRole.USER.value,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="true")
    timezone: Mapped[str | None] = mapped_column(String(64))
    locale: Mapped[str | None] = mapped_column(String(32))

    __table_args__ = (
        Index("ix_users_email", "email"),
        Index("ix_users_firebase_uid", "firebase_uid"),
    )
