from fastapi import APIRouter, Response
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_engine

router = APIRouter()


@router.get("/live", summary="Liveness check", tags=["health"])
def liveness() -> dict[str, str]:
    """Report that the API process is running."""
    return {"status": "alive"}


@router.get("/ready", summary="Readiness check", tags=["health"])
def readiness(response: Response) -> dict[str, object]:
    """Report readiness only when required configuration and database are available."""
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        response.status_code = 503
        return {
            "status": "not_ready",
            "checks": {"configuration": "ok", "database": "unavailable"},
        }

    return {"status": "ready", "checks": {"configuration": "ok", "database": "ok"}}
