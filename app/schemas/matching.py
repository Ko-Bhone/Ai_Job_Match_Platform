from pydantic import BaseModel, Field

class SkillMatchRequest(BaseModel):
    resume_skills: list [str] = Field(..., min_length=1, description="Skills extracted from the resume")
    job_skills : list [str] = Field(..., min_length=1, description="Skills required by the jobs")
