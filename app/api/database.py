from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.resume import Resume

router = APIRouter()

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
    return resumes
