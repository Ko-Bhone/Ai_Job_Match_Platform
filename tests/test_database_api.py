from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_database_health():
    response = client.get("/api/v1/database/health")
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == ("Database Connection Successfully!")

def test_get_resumes():
    response = client.get("/api/v1/database/resumes")
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == ("Resumes Retrieved Successfully!")
    assert "count" in data
    assert "resumes" in data
    assert isinstance(data["count"], int)
    assert isinstance(data["resumes"], list)

def test_get_jobs():
    response = client.get("/api/v1/database/jobs")
    assert response.status_code == 200
    data = response.json()
    assert data["Message"] == ("Jobs Retrieved Successfully!")
    assert "count" in data
    assert "jobs" in data
    assert isinstance(data["count"], int)
    assert isinstance(data["jobs"], list)