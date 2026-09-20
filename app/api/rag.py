from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.match_result import MatchResult
from app.services.rag_service import generate_recommendations


router = APIRouter()

@router.get("/recommendations/{match_result_id}", status_code=status.HTTP_200_OK)
def generate_recommendations(match_result_id: int, db: Session = Depends(get_db)):
    match_result = (db.query(MatchResult).filter(MatchResult.id == match_result_id).first())
    if not match_result:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Match result with id {match_result_id} not found"
        )
    missing_skills = match_result.missing_skills or []
    if not missing_skills:
        return {
            "Message": "No missing skills found",
            "match_result_id": match_result_id,
            "recommendations": []
        }
    recommendations = generate_recommendations(db=db, missing_skills=missing_skills)
    return {
        "Message":"RAG recommendations generated Successfully",
        "match_result_id": match_result_id,
        "resume_id": match_result.resume_id,
        "job_id": match_result.job_id,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }