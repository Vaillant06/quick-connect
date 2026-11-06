# QuickConnect

QuickConnect is a single-organization volunteer matching platform. See the [SRS](docs/SRS.md) and [Software Design](docs/Software-Design.md).

## Run the containerized skeleton locally

Requirements: Docker Engine with Docker Compose.

```sh
cp .env.compose.example .env
docker compose up --build
```

- Web app: <http://localhost>
- API documentation: <http://localhost:8000/docs>
- API readiness: <http://localhost:8000/api/v1/health/ready>

The Compose stack runs separate `frontend`, `backend`, `worker`, `migrate`, and `db` services. PostgreSQL data is kept in the `postgres_data` named volume across container restarts. The sample password is for local development only; use deployment secrets outside local development.

The frontend uses host port 80, FastAPI uses host port 8000, and PostgreSQL listens on its default port 5432 inside the Compose network. The database port is not published to the host.

Stop the stack with `docker compose down`. This preserves the database volume.
