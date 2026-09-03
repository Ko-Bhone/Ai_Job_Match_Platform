from fastapi import APIRouter
from app.api import resume, jobs, matching, rag
from app.api.jobs import router as jobs_router

api_router = APIRouter()

api_router.include_router(resume.router, prefix="/resume", tags=["Resumes"])

api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

api_router.include_router(matching.router, prefix="/matching", tags=["Matching"])

api_router.include_router(rag.router, prefix="/rag", tags=["RAG"])

api_router.include_router(resume.router, prefix="/resume", tags=["Resumes"])

api_router.include_router(jobs_router, prefix="/jobs", tags=["Jobs"])

api_router.include_router(matching.router, prefix="/matching", tags=["Matching"])