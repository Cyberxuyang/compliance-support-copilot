from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.llm.ollama import OllamaClient
from backend.app.core.config import settings


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    message: str
    sources: list[str]
    confidence: float


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:

    client = OllamaClient(
        base_url=settings.ollama_base_url,
        model=settings.ollama_model,
    )

    model_response = client.generate(request.message)

    return ChatResponse(
        message=model_response,
        sources=[],
        confidence=0.0,
    )
