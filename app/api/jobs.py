from fastapi import APIRouter, status, Depends
from app.schemas.job import JobDescriptionRequest
from app.services.text_cleaner import clean_text
from app.services.skill_extractor import extract_skills
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.job import Job

router = APIRouter()

@router.post("/analyze", status_code=status.HTTP_200_OK)

async def analyze_job(job: JobDescriptionRequest):
    "Analyze job description and extract required skills"

    raw_text = job.job_description
    cleaned_text = clean_text(raw_text)

    extracted_skills = extract_skills(cleaned_text)

    return {
        "message" : "Job description analyzed successfully",
        "job_description" : raw_text,
        "cleaned_text" : cleaned_text,
        "extracted_skills" : extracted_skills}

@router.post("/analyze")
def analyze_job(request : JobDescriptionRequest,
                db: Session = Depends(get_db)):
    return analyze_job(db=db)



