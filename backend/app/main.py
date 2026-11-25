from __future__ import annotations

import structlog
from fastapi import FastAPI

from app.api.v1 import api_router
from app.middleware import LoggingMiddleware, RateLimitMiddleware, SecurityHeadersMiddleware

structlog.configure(
	processors=[
		structlog.processors.TimeStamper(fmt="iso"),
		structlog.processors.add_log_level,
		structlog.processors.JSONRenderer(),
	]
)

app = FastAPI(title="Aegis AI API", version="0.1.0")

app.add_middleware(LoggingMiddleware)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimitMiddleware)

app.include_router(api_router, prefix="/api/v1")
