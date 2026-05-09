from fastapi import APIRouter
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    message: str
    sources: list[str]
    confidence: float


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(
        message=f"This is a mock response for: {request.message}",
        sources=[],
        confidence=0.0,
    )
