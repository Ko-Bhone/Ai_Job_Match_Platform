from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
    resume_id : int = Field(..., gt=0, description="Resume ID")
    job_id : int = Field(..., gt=0, description="Job ID")


