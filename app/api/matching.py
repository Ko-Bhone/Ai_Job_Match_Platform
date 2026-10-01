from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.matching import MatchRequest
from app.services.matching_services import create_match_result
from app.models.match_result import MatchResult

router = APIRouter()

@router.post("/match", status_code=status.HTTP_201_CREATED)
def match_resume_with_job(data: MatchRequest, db:Session=Depends(get_db)):
    return create_match_result(
        db=db,
        resume_id=data.resume_id,
        job_id=data.job_id)

@router.get("/{match_result_id}", status_code=status.HTTP_200_OK)
def get_match_result(match_result_id:int, db:Session=Depends(get_db)):
    match_result = db.query(MatchResult).filter(MatchResult.id == match_result_id).first()
    if not match_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Match result with id {match_result_id} not found!")
    return {
        "message" : "Match result retrieved Successfully",
        "match_result_id" : match_result.id,
        "resume_id" : match_result.resume_id,
        "job_id" : match_result.job_id,
        "matched_skills" : match_result.matched_skills,
        "missing_skills" : match_result.missing_skills,
        "extra_skills" : match_result.extra_skills,
        "skill_match_percentage" : match_result.skill_match_percentage,
        "text_similarity_percentage" : match_result.text_similarity_percentage,
        "skill_weight" : match_result.skill_weight,
        "similarity_weight" : match_result.similarity_weight,
        "final_match_score" : match_result.final_match_score,
        "created_at" : match_result.created_at
    }

