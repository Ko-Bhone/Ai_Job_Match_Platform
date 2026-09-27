from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.models.job import Job
from app.models.match_result import MatchResult
from app.services.skill_matcher import match_skills
from app.services.text_similarity import calculate_text_similarity
from app.services.match_score import calculate_final_match_score

def create_match_result(db: Session, resume_id: int, job_id: int) -> dict:

    #1. Get Resume
    resume = (db.query(Resume).filter(Resume.id == resume_id).first())
    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = "Resume with id {resume_id} not found!")

    #2. Get Job
    job = (db.query(Job).filter(Job.id == job_id).first())
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Job with id {job_id} not found!")

    #3. Validate Resume data
    if not resume.cleaned_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "Resume Cleaned Text is not provided!")
    if not resume.extracted_skills:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "Resume skills are Empty!")

    #4. Validate Job Data
    if not job.cleaned_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "Job Cleaned Text is not provided!")
    if not resume.extracted_skills:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "Resume skills are Empty!")

    #5. Skill Matching
    skill_result = match_skills(resume_skills = resume.extracted_skills, job_skills = job.extracted_skills)

    #6. Text Similarity
    similarity_result = calculate_text_similarity(
        resume_text = resume.cleaned_text,
        job_description = job.cleaned_text
    )

    #7. Final weight Score
    score_result = calculate_final_match_score(
        skill_match_percentage=skill_result["match_percentage"],
        text_similarity_percentage=similarity_result["similarity_percentage"]
    )

    #8. Create MatchResult
    match_result = MatchResult(
        resume_id = resume_id,
        job_id = job_id,
        matched_skills = skill_result["matched_skills"],
        missing_skills = skill_result["missing_skills"],
        extracted_skills = skill_result["extracted_skills"],
        skill_match_percentage = skill_result["skill_match_percentage"],
        text_similarity_percentage = skill_result["text_similarity_percentage"],
        skill_weight = score_result["skill_weight"],
        similarity_weight = score_result["similarity_weight"],
        final_match_score = score_result["final_match_score"]
    )

    #9 Save to Database
    try:
        db.add(match_result)
        db.commit()
        db.refresh(match_result)
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail = "Failed to save match result!") from exc

    #10. Response
    return {
        "message" : "Match result created successfully",
        "match_result_id" : match_result.id,
        "resume_id" : match_result.resume_id,
        "job_id" : match_result.job_id,
        "matched_skills" : match_result.matched_skills,
        "missing_skills" : match_result.missing_skills,
        "extra_skills" : match_result.extra_skills,
        "skill_match_percentage" : match_result.skill_match_percentage,
        "similarity_score" : similarity_result["similarity_score"],
        "text_similarity_percentage" : match_result.text_similarity_percentage,
        "skill_weight" : match_result.skill_weight,
        "similarity_weight" : match_result.similarity_weight,
        "final_match_score" : match_result.final_match_score
    }