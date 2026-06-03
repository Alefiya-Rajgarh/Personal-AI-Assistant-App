# AI Executive Assistant Monorepo

This monorepo contains the production-ready backend and mobile app for the Assistant AI platform.

## Structure

- `backend/`: FastAPI clean-architecture backend (Poetry-managed)
- `mobile/`: Flutter application

## Quick start

1. Copy environment variables.
2. Start services with Docker Compose.

```sh
cp backend/.env.example backend/.env

docker compose up --build
```
