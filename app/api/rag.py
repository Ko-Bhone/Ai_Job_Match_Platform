from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def rag_health():
    return {
        "Message": "Rag Service is Ready.."
    }