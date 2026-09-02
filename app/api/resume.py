from fastapi import APIRouter
import shutil
import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.services.resume_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = Path("uploads/resume")
UPLOAD_DIR.mkdir(parents=True, exist_ok = True)

@router.post("/upload", status_code=status.HTTP_201_CREATED)

async def upload_resume(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File name is missing")

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files are allowed")

    file_extension = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    file_path = UPLOAD_DIR / unique_filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)
    if not extracted_text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not extract text form this pdf")

    return {
        "Message": "Resume Uploaded Successfully",
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "content_type": file.content_type,
        "extracted_text": extracted_text
    }


