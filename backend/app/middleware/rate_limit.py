from __future__ import annotations

import time

import redis.asyncio as redis
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from app.core.config import get_settings

AI_PATH_PREFIXES = ("/api/v1/ai", "/api/v1/agents", "/api/v1/chat")


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        settings = get_settings()
        self.redis = redis.from_url(str(settings.redis_url), decode_responses=True)

    async def dispatch(self, request: Request, call_next) -> Response:
        client_host = request.client.host if request.client else "unknown"
        user_key = (
            request.headers.get("X-User-Id")
            or getattr(request.state, "user_id", None)
            or client_host
        )
        now = int(time.time())
        limit = 20 if request.url.path.startswith(AI_PATH_PREFIXES) else 100
        window = 60
        key = f"rate:{user_key}:{'ai' if limit == 20 else 'default'}"

        pipeline = self.redis.pipeline()
        pipeline.zremrangebyscore(key, 0, now - window)
        pipeline.zadd(key, {str(now): now})
        pipeline.zcard(key)
        pipeline.expire(key, window)
        _, _, count, _ = await pipeline.execute()

        if count and int(count) > limit:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded"},
            )

        return await call_next(request)
