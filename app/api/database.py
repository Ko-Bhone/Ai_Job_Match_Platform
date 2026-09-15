from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.resume import Resume

router = APIRouter(prefix="/database", tags=["Database"])

@router.get("/health")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"Message": "Database Connection Successfully!"}
    except Exception as error:
        return {"Message" : "Database Connection Failed!", "error": str(error)}

@router.get("/resumes")
def get_resumes(db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()
    return {
        "Message" : "Resumes Retrieved Successfully!",
        "count" : len(resumes),
        "resumes" : resumes
    }

@router.get("/resumes/{resume_id}")
def get_resume(resume_id : int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {
        "Message" : "Resume Retrieved Successfully!",
        "resume" : resume
    }
