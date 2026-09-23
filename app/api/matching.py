from fastapi import (APIRouter, status, Depends, HTTPException)
from sqlalchemy.orm import Session
from app.schemas.matching import (SkillMatchRequest, MatchRequest)
from app.services.skill_matcher import (match_skills as calculate_skill_match)
from app.services.text_similarity import (calculate_text_similarity)
from app.database.session import get_db
from app.models.resume import Resume
from app.models.job import Job
from app.models.match_result import MatchResult

router = APIRouter()

@router.get("/")
def get_matches():
    return {"Message": "Get job Matches"}

@router.post("/match", status_code=status.HTTP_201_CREATED)
def create_match_result(data: MatchRequest, db: Session = Depends(get_db)):
    # 1. Get Resume from Database
    resume = (db.query(Resume).filter(Resume.id == data.resume_id).first())
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found")

    # 2. Get Job from Database
    job = (db.query(Job).filter(Job.id == data.job_id).first())
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found")

    # 3. Validate Resume Data
    if not resume.cleaned_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Resume cleaned text is empty")
    if not resume.extracted_skills:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Resume skills are empty")

    # 4. Validate Job Data
    if not job.cleaned_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Job cleaned text is empty")
    if not job.extracted_skills:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Job skills are empty")

    # 5. Skill Matching
    skill_result = calculate_skill_match(
        resume_skills=resume.extracted_skills,
        job_skills=job.extracted_skills)
    matched_skills = skill_result["matched_skills"]
    missing_skills = skill_result["missing_skills"]
    extra_skills = skill_result["extra_skills"]
    skill_match_percentage = skill_result["match_percentage"]

    # 6. Text Similarity
    similarity_result = calculate_text_similarity(
        resume_text=resume.cleaned_text,
        job_description=job.cleaned_text)
    similarity_score = similarity_result["similarity_score"]
    text_similarity_percentage = (
        similarity_result["similarity_percentage"])

    # 7. Weighted Scoring
    skill_weight = 0.70
    similarity_weight = 0.30
    final_match_score = (
        skill_match_percentage * skill_weight + text_similarity_percentage * similarity_weight)
    final_match_score = float(round(final_match_score, 2))

    # 8. Create Match Result
    match_result = MatchResult(
        resume_id=data.resume_id,
        job_id=data.job_id,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        extra_skills=extra_skills,
        skill_match_percentage=skill_match_percentage,
        text_similarity_percentage=text_similarity_percentage,
        skill_weight=skill_weight,
        similarity_weight=similarity_weight,
        final_match_score=final_match_score
    )

    # 9. Save to Database
    db.add(match_result)
    db.commit()
    db.refresh(match_result)

    # 10. Return Result
    return {
        "message": "Match result created successfully",
        "match_result_id": match_result.id,
        "resume_id": match_result.resume_id,
        "job_id": match_result.job_id,
        "matched_skills": match_result.matched_skills,
        "missing_skills": match_result.missing_skills,
        "extra_skills": match_result.extra_skills,
        "skill_match_percentage": match_result.skill_match_percentage,
        "similarity_score": similarity_score,
        "text_similarity_percentage": match_result.text_similarity_percentage,
        "skill_weight": match_result.skill_weight,
        "similarity_weight": match_result.similarity_weight,
        "final_match_score": match_result.final_match_score
    }