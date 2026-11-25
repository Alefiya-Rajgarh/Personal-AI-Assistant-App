from __future__ import annotations

import base64
import hashlib

from cryptography.fernet import Fernet

from app.core.config import get_settings


def _derive_key(secret: str) -> bytes:
    digest = hashlib.sha256(secret.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


def _get_fernet() -> Fernet:
    settings = get_settings()
    key = _derive_key(settings.secret_key.get_secret_value())
    return Fernet(key)


def encrypt_token(value: str) -> str:
    fernet = _get_fernet()
    return fernet.encrypt(value.encode("utf-8")).decode("utf-8")


def decrypt_token(value: str) -> str:
    fernet = _get_fernet()
    return fernet.decrypt(value.encode("utf-8")).decode("utf-8")
