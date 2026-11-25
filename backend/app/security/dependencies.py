from __future__ import annotations

from typing import Callable

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.core.database import get_async_session
from app.models.user import User, UserRole
from app.security.firebase_auth import verify_firebase_token

security_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
    session: AsyncSession = Depends(get_async_session),
    request: Request | None = None,
) -> User:
    payload = await verify_firebase_token(credentials.credentials)
    firebase_uid = payload.get("uid")
    if not firebase_uid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Firebase token payload",
        )

    result = await session.execute(select(User).where(User.firebase_uid == firebase_uid))
    user = result.scalar_one_or_none()

    if user is None:
        email = payload.get("email") or f"{firebase_uid}@firebase.local"
        user = User(
            firebase_uid=firebase_uid,
            email=email,
            full_name=payload.get("name") or payload.get("displayName"),
            avatar_url=payload.get("picture"),
            role=UserRole.USER,
            is_active=True,
            locale=payload.get("locale"),
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    if user.deleted_at is not None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    if request is not None:
        request.state.user_id = str(user.id)

    return user


def require_role(roles: list[str]) -> Callable:
    async def _dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role.value not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return current_user

    return _dependency
