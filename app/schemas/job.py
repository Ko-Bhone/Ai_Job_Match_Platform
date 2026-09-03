from pydantic import BaseModel, Field

class JobDescriptionRequest(BaseModel):
    job_description: str = Field(..., min_length=20, description="job description text")
