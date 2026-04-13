# AI Task Board

Kanban board with AI-powered task analysis. Vue 3 + FastAPI + PostgreSQL + Redis.

## Getting started

Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY`.

```bash
cp .env.example .env
```

First run:

```bash
docker compose up db redis -d
docker compose run --rm api alembic upgrade head
docker compose up api
```

After that:

```bash
docker compose up
```

API runs on `http://localhost:8000`, docs at `/docs`.
