from fastapi import FastAPI

from backend.app.core.config import settings

app = FastAPI(title="Compliance Support Copilot")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "compliance-support-copilot",
        "env": settings.app_env,
    }
