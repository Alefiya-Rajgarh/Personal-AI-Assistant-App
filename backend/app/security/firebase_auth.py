from __future__ import annotations

import asyncio

import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException, status

from app.core.config import get_settings


def _get_firebase_app() -> firebase_admin.App:
    settings = get_settings()
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(str(settings.firebase_credentials))
        return firebase_admin.initialize_app(cred)


async def verify_firebase_token(token: str) -> dict:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token",
        )

    def _verify() -> dict:
        app = _get_firebase_app()
        return auth.verify_id_token(token, app=app)

    try:
        return await asyncio.to_thread(_verify)
    except Exception as exc:  # pragma: no cover - mapped to 401
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        ) from exc
