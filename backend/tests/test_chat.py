from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_chat_returns_mock_response() -> None:
    response = client.post(
        "/chat",
        json={"message": "Can I get a refund after 14 days?"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "This is a mock response for: Can I get a refund after 14 days?",
        "sources": [],
        "confidence": 0.0,
    }
