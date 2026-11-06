# QuickConnect backend

FastAPI API and separate worker entry point, using PostgreSQL/PostGIS through SQLAlchemy and Alembic migrations.

## Requirements

- Python 3.11 or newer
- uv

## Local development

```sh
uv sync
cp .env.example .env
uv run uvicorn app.main:app --reload
```

The API exposes `GET /api/v1/health/live` and `GET /api/v1/health/ready`. Readiness returns HTTP 503 until the configured PostgreSQL database accepts a connection. Interactive API documentation is available at `/docs` during local development.

## Database

Set `QC_DATABASE_URL` to a PostgreSQL URL using the `psycopg` driver. The default points at a local database; the database container and Compose configuration will be added in the containerization step.

Run database migrations with:

```sh
uv run alembic upgrade head
```

The initial migration enables the PostGIS extension. Database models and schema migrations will be introduced with the relevant feature work.

Run the worker skeleton separately with:

```sh
uv run python -m app.worker
```

Environment variables use the `QC_` prefix. See `.env.example` for the initial settings.
