from pydantic import BaseModel, Field

class JobAnalyzeRequest(BaseModel):
    job_description: str = Field(..., min_length=20, description="job description text")
