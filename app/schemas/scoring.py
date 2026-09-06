from pydantic import BaseModel, Field

class MatchScoreRequest(BaseModel):
    skill_match_percentage : float = Field(..., ge=0, le=100, description="Skill matching percentage")
    text_similarity_percentage: float = Field(..., ge=0, le=100, description="TF-IDF cosine similarity percentage")
