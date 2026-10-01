from app.services.skill_matcher import match_skills

def test_match_skills_all_match():
    result = match_skills(
        resume_skills = ["python", "fastapi", "docker"],
        job_skills = ["python", "fastapi", "docker"]
    )

    assert result ["matched_skills"] == ["docker", "fastapi", "python"]
    assert result ["missing_skills"] == []
    assert result["extra_skills"] == []
    assert result ["match_percentage"] == 100.0

def test_match_skills_partial_match():
    result = match_skills(
        resume_skills = ["python", "fastapi"],
        job_skills = ["python", "fastapi", "docker", "aws"]
    )
    assert result["matched_skills"] == ["fastapi", "python"]
    assert result["missing_skills"] == ["aws","docker"]
    assert result["extra_skills"] == []
    assert result["match_percentage"] == 50.0

def test_match_skills_with_extra_skills():
    result = match_skills(
        resume_skills = ["python", "fastapi", "pytorch"],
        job_skills = ["python", "fastapi"]
    )
    assert result ["matched_skills"] == ["fastapi", "python"]
    assert result["missing_skills"] == []
    assert result["extra_skills"] == ["pytorch"]
    assert result["match_percentage"] == 100.0

def test_match_skills_empty_job_skills():
    result = match_skills(
        resume_skills = ["python"],
        job_skills = []
    )

    assert result ["matched_skills"] == []
    assert result ["missing_skills"] == []
    assert result ["extra_skills"] == ["python"]
    assert result ["match_percentage"] == 0.0
