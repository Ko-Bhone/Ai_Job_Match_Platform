from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.job import JobDescriptionRequest
from app.services.text_cleaner import clean_text
from app.services.skill_extractor import extract_skills
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.job import Job

router = APIRouter()

@router.post("/analyze", status_code=status.HTTP_200_OK)

async def analyze_job(job: JobDescriptionRequest, db: Session = Depends(get_db)):
    "Analyze job description and extract required skills"

    #1. Get raw job description
    raw_text = job.job_description

    #2. Clean text
    cleaned_text = clean_text(raw_text)

    #3. Extract skills
    extracted_skills = extract_skills(cleaned_text)

    #4. Create job Database object
    new_job = Job(
        job_description = raw_text,
        cleaned_text = cleaned_text,
        extracted_skills = extracted_skills
    )

    #5. Save to Postgresql
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    #6. Return Response
    return {
        "Message" : "Job Description analyzed successfully!",
        "job_id" : new_job.id,
        "job_description" : raw_text,
        "cleaned_text" : cleaned_text,
        "extracted_skills" : extracted_skills
    }