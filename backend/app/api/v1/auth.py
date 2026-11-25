from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_async_session
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.security.dependencies import get_current_user
from app.security.firebase_auth import verify_firebase_token

router = APIRouter(prefix="/auth", tags=["auth"])
security_scheme = HTTPBearer()


@router.post("/register", response_model=UserResponse)
async def register_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.post("/refresh")
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> dict:
    payload = await verify_firebase_token(credentials.credentials)
    return {
        "firebase_uid": payload.get("uid"),
        "email": payload.get("email"),
        "issued_at": datetime.fromtimestamp(payload.get("iat", 0)).isoformat(),
        "expires_at": datetime.fromtimestamp(payload.get("exp", 0)).isoformat(),
    }


@router.get("/me", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.put("/me", response_model=UserResponse)
async def update_profile(
    payload: UserUpdate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> User:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(current_user, field, value)

    await session.commit()
    await session.refresh(current_user)
    return current_user


@router.delete("/me")
async def delete_profile(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    current_user.deleted_at = datetime.now(tz=timezone.utc)
    current_user.is_active = False
    await session.commit()
    return {"status": "deleted"}
