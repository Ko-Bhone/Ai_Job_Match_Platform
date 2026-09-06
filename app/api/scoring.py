from fastapi import APIRouter, status
from app.schemas.scoring import MatchScoreRequest
from app.services.match_score import calculate_final_match_score

router = APIRouter()

@router.post("/final-score", status_code=status.HTTP_200_OK)
async def calculate_final_score(data: MatchScoreRequest):
    result =  calculate_final_match_score(
        skill_match_percentage = data.skill_match_percentage,
        text_similarity_percentage = data.text_similarity_percentage
    )

    return {
        "Message" : "Final Match Score Calculated Successfully", **result
    }