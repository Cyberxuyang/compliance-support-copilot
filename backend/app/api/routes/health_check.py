from fastapi import APIRouter

from backend.app.core.config import settings


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "compliance-support-copilot",
        "environment": settings.app_env,
    }
