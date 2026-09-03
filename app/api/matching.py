from fastapi import APIRouter, status
from app.schemas.matching import SkillMatchRequest
from app.services.skill_matcher import match_skills

router = APIRouter()

@router.get("/")
def get_matches():
    return {
        "Message": "Get job Matches"
    }

@router.post("/skills", status_code=status.HTTP_200_OK)
async def match_resume_with_job(data: SkillMatchRequest):
    result = match_skills(resume_skills=data.resume_skills, job_skills=data.job_skills)

    return {
        "Message": "Skill matching completed Successfully", **result
    }
