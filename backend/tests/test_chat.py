from fastapi.testclient import TestClient

from backend.app.llm.ollama import OllamaClient
from backend.app.main import app


client = TestClient(app)


def test_chat_returns_llm_response(monkeypatch) -> None:
    def fake_generate(self, prompt: str) -> str:
        return f"Fake LLM response for: {prompt}"

    monkeypatch.setattr(OllamaClient, "generate", fake_generate)

    response = client.post(
        "/chat",
        json={"message": "Can I get a refund after 14 days?"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Fake LLM response for: Can I get a refund after 14 days?",
        "sources": [],
        "confidence": 0.0,
    }
