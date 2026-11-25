from __future__ import annotations

import time
import uuid

import structlog
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = structlog.get_logger("aegis.request")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        trace_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.trace_id = trace_id

        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000

        user_id = getattr(request.state, "user_id", None)

        logger.info(
            "request",
            trace_id=trace_id,
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=round(duration_ms, 2),
            user_id=user_id,
        )

        response.headers["X-Request-ID"] = trace_id
        return response
