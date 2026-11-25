from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: AnyUrl
    redis_url: AnyUrl
    openai_api_key: SecretStr
    firebase_credentials_path: Path
    google_client_id: str
    google_client_secret: SecretStr
    aws_access_key_id: SecretStr
    aws_secret_access_key: SecretStr
    aws_region: str
    sentry_dsn: str | None = None
    secret_key: SecretStr

    @property
    def firebase_credentials(self) -> Path:
        if not self.firebase_credentials_path.exists():
            raise FileNotFoundError(
                f"Firebase credentials not found at {self.firebase_credentials_path}"
            )
        return self.firebase_credentials_path

    def redact(self) -> dict[str, Any]:
        return {
            "database_url": str(self.database_url),
            "redis_url": str(self.redis_url),
            "openai_api_key": "***",
            "firebase_credentials_path": str(self.firebase_credentials_path),
            "google_client_id": self.google_client_id,
            "google_client_secret": "***",
            "aws_access_key_id": "***",
            "aws_secret_access_key": "***",
            "aws_region": self.aws_region,
            "sentry_dsn": self.sentry_dsn,
            "secret_key": "***",
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()
