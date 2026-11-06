from fastapi import FastAPI

from app.api.v1.router import api_router
from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="QuickConnect volunteer matching platform API.",
)
app.include_router(api_router, prefix=settings.api_prefix)
