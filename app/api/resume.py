from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_resume():
    return {
        "Message": "Get All Resumes."
    }