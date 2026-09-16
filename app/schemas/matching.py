from pydantic import BaseModel, Field

class SkillMatchRequest(BaseModel):
    resume_skills: list [str] = Field(..., min_length=1, description="Skills extracted from the resume")
    job_skills : list [str] = Field(..., min_length=1, description="Skills required by the jobs")
    resume_id: int
    job_id: int
    resume_text: str = Field(..., min_length=1, description="Cleaned resume text")
    job_description: str = Field(..., min_length=1, description="Job description")



