from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_missing_match_results():
    response = client.get("/api/v1/matching/2147483647")

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == ("Match result with id 2147483647 not found!")

def test_match_with_missing_resume():
    response = client.post("/api/v1/matching/match", json={"resume_id":2147483647,
                                                                "job_id":2147483647})
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == ("Resume with id 2147483647 not found!")