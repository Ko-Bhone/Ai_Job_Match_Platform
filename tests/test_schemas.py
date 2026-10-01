import pytest
from pydantic import ValidationError
from app.schemas.matching import MatchRequest
from app.schemas.job import JobAnalyzeRequest
from app.schemas.scoring import MatchScoreRequest

def test_valid_match_request():
    data = MatchRequest(
        resume_id= 1,
        job_id = 1
    )
    assert data.resume_id == 1
    assert data.job_id == 1

def test_invalid_match_request():
    with pytest.raises(ValidationError):
        MatchRequest(
            resume_id= 0,
            job_id = 1
        )

def test_missing_match_request_field():
    with pytest.raises(ValidationError):
        MatchRequest(resume_id=1)

def test_valid_job_request():
    data = JobAnalyzeRequest(
        job_description="Python FastAPI machine learning developer"
    )
    assert "Python" in data.job_description

def test_invalid_short_job_request():
    with pytest.raises(ValidationError):
        JobAnalyzeRequest(job_description="abc")

def test_valid_score_request():
    data = MatchScoreRequest(
        skill_match_percentage = 80,
        text_similarity_percentage = 60
    )

    assert data.skill_match_percentage == 80
    assert data.text_similarity_percentage == 60

def test_invalid_score_above_100():
    with pytest.raises(ValidationError):
        MatchScoreRequest(
            skill_match_percentage = 120,
            text_similarity_percentage = 60
        )

def test_invalid_negative_score():
    with pytest.raises(ValidationError):
        MatchScoreRequest(
            skill_match_percentage = -1,
            text_similarity_percentage = 60
        )