from fastapi import APIRouter, status

from app.schemas.similarity import TextSimilarityRequest
from app.services.text_similarity import calculate_text_similarity

router = APIRouter()

@router.post("/text", status_code= status.HTTP_200_OK)

async def calculate_similarity(data: TextSimilarityRequest):
    result = calculate_text_similarity(resume_text=data.resume_text, job_description= data.job_description)
    return {"message": "Text similarity calculated successfully!", **result}

