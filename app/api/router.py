from fastapi import APIRouter
from app.api import resume, jobs, matching, similarity, scoring, database, rag

api_router = APIRouter()

api_router.include_router(resume.router, prefix="/resume", tags=["Resume"])

api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

api_router.include_router(matching.router, prefix="/matching", tags=["Matching"])

api_router.include_router(similarity.router, prefix="/similarity", tags=["Similarity"])

api_router.include_router(scoring.router, prefix="/scoring", tags=["Scoring"])

api_router.include_router(database.router, prefix="/database", tags=["Database"])

api_router.include_router(rag.router, prefix="/rag", tags=["RAG"])