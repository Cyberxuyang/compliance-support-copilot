from fastapi import FastAPI

from backend.app.api.routes.health_check import router as health_router
from backend.app.api.routes.chat import router as chat_router

app = FastAPI(title="Compliance Support Copilot")

app.include_router(health_router)
app.include_router(chat_router)
