from pydantic import BaseModel, Field


class TextSimilarityRequest(BaseModel):
    resume_text: str = Field(..., min_length=10, description= "Cleaned or original resume text")
    job_description: str = Field(..., min_length=10, description = "Job description text")
