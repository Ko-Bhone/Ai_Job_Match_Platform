from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == ("AI Job Match Platform is Running....")

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Healthy"

def test_final_score_api():
    response = client.post(
        "/api/v1/scoring/final-score",
        json={
            "skill_match_percentage": 80,
            "text_similarity_percentage": 60
        }
    )

    assert response.status_code == 200
    data = response.json()
    print(response.json())
    assert data["message"] == ("Final match score calculated successfully")
    assert data["skill_match_percentage"] == 80.0
    assert data["text_similarity_percentage"] == 60.0
    assert data["skill_weight"] == 0.70
    assert data["similarity_weight"] == 0.30
    assert data["weighted_skill_score"] == 56.0
    assert data["weighted_similarity_score"] == 18.0
    assert data["final_match_score"] == 74.0

def test_final_score_invalid_percentage():
    response = client.post(
        "/api/v1/scoring/final-score",
        json={
            "skill_match_percentage": 120,
            "text_similarity_percentage": 60
        }
    )
    assert response.status_code == 422

def test_final_score_negative_percentage():
    response = client.post(
        "/api/v1/scoring/final-score",
        json={
            "skill_match_percentage": -10,
            "text_similarity_percentage": 60
        }
    )
    assert response.status_code == 422

def test_final_score_missing_field():
    response = client.post(
        "/api/v1/scoring/final-score",
        json={
            "skill_match_percentage": 80
        }
    )
    assert response.status_code == 422