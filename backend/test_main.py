import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_health():
    """Test that the API is accessible"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_scrape_endpoint_validation():
    """Test scrape endpoint with valid data"""
    response = client.post("/scrape", json={
        "url": "https://example.com",
        "use_js": False,
        "doc_types": ["pdf"]
    })
    assert response.status_code == 200
    assert "job_id" in response.json()

def test_score_text_endpoint():
    """Test AI text scoring endpoint"""
    response = client.post("/score-text", data={
        "text": "This is a test sentence for scoring."
    })
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "label" in data
    assert 1 <= data["score"] <= 100

def test_deai_text_endpoint():
    """Test De-AI text endpoint"""
    response = client.post("/deai-text", data={
        "text": "This is formal AI-generated text.",
        "level": "2"
    })
    assert response.status_code == 200
    data = response.json()
    assert "deai_text" in data
    assert len(data["deai_text"]) > 0
