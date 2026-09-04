from fastapi import APIRouter
import shutil
import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.services.resume_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.skill_extractor import extract_skills

router = APIRouter()
UPLOAD_DIR = Path("uploads/resume")
UPLOAD_DIR.mkdir(parents=True, exist_ok = True)

@router.post("/upload", status_code=status.HTTP_201_CREATED)

async def upload_resume(file: UploadFile = File(...)):
    #1.validate filename
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File name is missing")

    #2. validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files are allowed")

    #3.Create unique filename
    file_extension = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    #4.Create file path
    file_path = UPLOAD_DIR / unique_filename

    #5.Save pdf
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #6.Extract text
    extracted_text = extract_text_from_pdf(file_path)

    #7.Validate extracted text
    if not extracted_text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not extract text form this pdf")

    #8.Clean text
    cleaned_text = clean_text(extracted_text)

    #9. Extract skills
    extracted_skills = extract_skills(cleaned_text)

    return {
        "Message": "Resume Uploaded Successfully",
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "content_type": file.content_type,
        "extracted_text": extracted_text,
        "cleaned_text": cleaned_text,
        "extracted_skills": extracted_skills}


