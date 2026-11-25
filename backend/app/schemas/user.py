from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.user import UserRole


class UserResponse(BaseModel):
    id: UUID
    firebase_uid: str
    email: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    role: UserRole
    is_active: bool
    timezone: Optional[str] = None
    locale: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    timezone: Optional[str] = None
    locale: Optional[str] = None
