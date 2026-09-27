from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.matching import MatchRequest
from app.services.matching_services import create_match_result

router = APIRouter()

@router.post("/match", status_code=status.HTTP_201_CREATED)
def match_resume_with_job(data: MatchRequest, db:Session=Depends(get_db)):
    return create_match_result(
        db=db,
        resume_id=data.resume_id,
        job_id=data.job_id
    )