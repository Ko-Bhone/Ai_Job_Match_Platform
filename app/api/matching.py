from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.matching import SkillMatchRequest
from app.services.skill_matcher import match_skills as calculate_skill_match
from app.database.session import get_db
from app.models.match_result import MatchResult
from app.services.text_similarity import calculate_text_similarity

router = APIRouter()

@router.get("/")
def get_matches():
    return {"Message": "Get job Matches"}

@router.post("/skills", status_code=status.HTTP_200_OK)
async def match_resume_with_job(data: SkillMatchRequest):
    """
    Compare resume skills with job skills.
    """
    result = calculate_skill_match(
        resume_skills=data.resume_skills,
        job_skills=data.job_skills
    )
    return {"Message": "Skill matching completed Successfully", **result}

@router.post("/match", status_code=status.HTTP_201_CREATED)
def create_match_result(
    data: SkillMatchRequest, db: Session = Depends(get_db)):
    """
    Calculate skill match and save the result to PostgreSQL.
    """

    # 1. Calculate skill matching
    result = calculate_skill_match(
        resume_skills=data.resume_skills,
        job_skills=data.job_skills
    )

    # 2. Get matching results
    matched_skills = result["matched_skills"]
    missing_skills = result["missing_skills"]
    extra_skills = result["extra_skills"]
    skill_match_percentage = result["match_percentage"]

    # Text Similarity
    similarity_result = calculate_text_similarity(
        resume_text = data.resume_text,
        job_description = data.job_description
    )
    text_similarity_percentage = (similarity_result["similarity_percentage"])
    similarity_score = similarity_result["similarity_score"]

    #3. Weighted Scoring
    skill_weight = 0.70
    similarity_weight = 0.30
    text_similarity_percentage = 0.0
    final_match_score = (
        skill_match_percentage * skill_weight + text_similarity_percentage * similarity_weight)
    final_match_score = round(final_match_score, 2)

    #4. Create MatchResult
    match_result = MatchResult(
        resume_id = data.resume_id,
        job_id = data.job_id,
        matched_skills = matched_skills,
        missing_skills = missing_skills,
        extra_skills = extra_skills,
        skill_match_percentage = skill_match_percentage,
        text_similarity_percentage = text_similarity_percentage,
        skill_weight = skill_weight,
        similarity_weight = similarity_weight,
        final_match_score = round(final_match_score, 2),
    )

    db.add(match_result)
    db.commit()
    db.refresh(match_result)


    # 5. Return response
    return {
        "Message": "Match Result saved Successfully",
        "match_result_id" : match_result.id,
        "resume_id" : match_result.resume_id,
        "job_id" : match_result.job_id,
        "matched_skills" : match_result.matched_skills,
        "missing_skills" : match_result.missing_skills,
        "extra_skills" : match_result.extra_skills,
        "skill_match_percentage" : match_result.skill_match_percentage,
        "similarity_score" : round(similarity_score, 2),
        "text_similarity_percentage" : match_result.text_similarity_percentage,
        "skill_weight" : match_result.skill_weight,
        "similarity_weight" : match_result.similarity_weight,
        "final_match_score" : match_result.final_match_score,
    }