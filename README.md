# AI Job Match & Career Intelligence Platform

An AI-powered job matching and career intelligence platform that analyzes resumes against job descriptions, calculates job-fit scores, identifies missing skills, and provides learning recommendations using NLP, Machine Learning, Sentence Transformers, PostgreSQL, pgvector, and RAG.
---
## 🚀 Project Overview
The **AI Job Match & Career Intelligence Platform** is an end-to-end AI engineering project designed to demonstrate how Machine Learning, NLP, vector search, and RAG can be combined into a practical career and recruitment-related application.
The system takes:
- A candidate resume
- A job description

and processes them through:
```text
Resume + Job Description
            │
            ▼
      PDF Text Extraction
            │
            ▼
        NLP Cleaning
            │
            ▼
       Skill Extraction
            │
            ▼
      Skill Matching
            │
            ├───────────────┐
            ▼               ▼
       Skill Score      TF-IDF
                            │
                            ▼
                   Cosine Similarity
                            │
            └───────┬───────┘
                    ▼
             Weighted Score
                    │
                    ▼
              Missing Skills
                    │
                    ▼
             Vector Search
                    │
                    ▼
           RAG Recommendations

✨ Key Features
1. Resume Upload
Upload a candidate resume in PDF format.
The system:
Accepts PDF files
Extracts text from the PDF
Cleans the extracted text
Extracts relevant technical skills
Stores resume information in PostgreSQL

2. Job Description Analysis
The system analyzes a job description and extracts relevant skills.
Example:    Python, FastAPI, Machine Learning, Scikit-learn, NLP, PostgreSQL, Docker, AWS, RAG
The analyzed job description can also be stored in PostgreSQL.

3. NLP Skill Extraction
The project includes NLP-based text processing for identifying technical skills from: Resumes, Job descriptions
The extracted skills are normalized and used for matching.

4. Skill Matching
The candidate's skills are compared with the required job skills.
The system identifies: Matched Skills, Missing Skills, Extra Skills, Skill Match Percentage
Example:
Matched Skills
--------------
Python
FastAPI
Machine Learning
Scikit-learn
Docker
PostgreSQL

Missing Skills
--------------
AWS
NLP
RAG

5. TF-IDF Text Similarity
The platform uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert resume and job-description text into numerical vectors.
It then uses Cosine Similarity to measure textual similarity between the resume and job description.
Example:
Similarity Score:       0.6424
Similarity Percentage: 64.24%

6. Weighted Match Score
The final matching score combines:
Skill Match Percentage
Text Similarity Percentage
Current weighting:
Skill Matching      = 70%
Text Similarity     = 30%
Formula:
Final Score =
    (Skill Match × 0.70)
    +
    (Text Similarity × 0.30)
Example:
Skill Match:          66.67%
Text Similarity:      64.24%
Final Match Score:    65.94%

7. PostgreSQL Database
PostgreSQL is used for persistent storage.
The project uses SQLAlchemy ORM to communicate with PostgreSQL.
Main database entities include: resumes, jobs, match_results, knowledge_chunks
The database stores:
Resume information
Extracted resume text
Extracted skills
Job descriptions
Extracted job skills
Match results
Missing skills
Match scores
Knowledge chunks
Vector embeddings

8. Sentence Transformers
The project uses:
all-MiniLM-L6-v2
from Sentence Transformers to generate text embeddings.
These embeddings are used for semantic similarity search.

9. pgvector
PostgreSQL + pgvector is used for vector storage and similarity search.
The architecture allows knowledge embeddings to be stored directly inside PostgreSQL.
Example:
Knowledge
    │
    ▼
Text Chunking
    │
    ▼
Sentence Transformer
    │
    ▼
Embedding Vector
    │
    ▼
PostgreSQL + pgvector

10. RAG-Based Career Recommendations
The project includes a Retrieval-Augmented recommendation pipeline.
When a candidate is missing skills, the system retrieves relevant learning knowledge from the vector database.
Example:
Missing Skill
     │
     ▼
AWS
     │
     ▼
Create Query Embedding
     │
     ▼
pgvector Similarity Search
     │
     ▼
AWS Fundamentals
     │
     ▼
Learning Recommendation
The current implementation focuses on retrieval and recommendation, rather than using an external generative LLM.

🧠 Technology Stack
Backend
Python
FastAPI
Uvicorn
Pydantic
Machine Learning
Scikit-learn
TF-IDF
Cosine Similarity
Feature-based matching
NLP
Text preprocessing
Skill extraction
Text similarity
Semantic embeddings
Deep Learning / Embeddings
Sentence Transformers
all-MiniLM-L6-v2
PyTorch
Database
PostgreSQL
SQLAlchemy
pgvector
JSONB
RAG
Text chunking
Embeddings
Vector search
Retrieval-based recommendations
Testing
Pytest
HTTPX
Development
Git
GitHub
Swagger / OpenAPI

📁 Project Structure
Ai_Job_Match_Platform/
│
├── app/
│   ├── api/
│   │   ├── resume.py
│   │   ├── jobs.py
│   │   ├── matching.py
│   │   ├── rag.py
│   │   ├── similarity.py
│   │   ├── scoring.py
│   │   ├── database.py
│   │   └── router.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── resume.py
│   │   ├── job.py
│   │   ├── match_result.py
│   │   └── knowledge.py
│   │
│   ├── schemas/
│   │   ├── job.py
│   │   ├── matching.py
│   │   ├── similarity.py
│   │   └── scoring.py
│   │
│   └── services/
│       ├── text_cleaner.py
│       ├── skill_extractor.py
│       ├── skill_matcher.py
│       ├── text_similarity.py
│       ├── match_scorer.py
│       ├── knowledge_loader.py
│       ├── text_chunker.py
│       ├── embedding_service.py
│       ├── vector_search.py
│       ├── knowledge_service.py
│       ├── seed_knowledge.py
│       └── rag_service.py
│
├── data/
│   └── career_knowledge.json
│
├── tests/
│
├── uploads/
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
🔄 System Workflow

The complete Version 1 workflow is:
                    ┌─────────────────┐
                    │  Resume PDF     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ PDF Extraction  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ NLP Processing  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Skill Extraction│
                    └────────┬────────┘
                             │
                             │
Job Description ─────────────┤
                             │
                             ▼
                    ┌─────────────────┐
                    │ Skill Matching  │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              Skill Score        TF-IDF
                                      │
                                      ▼
                              Cosine Similarity
                                      │
                    ┌─────────┬───────┘
                    ▼         ▼
               Skill %    Similarity %
                    │         │
                    └────┬────┘
                         ▼
                 Weighted Score
                         │
                         ▼
                  Missing Skills
                         │
                         ▼
                  Vector Search
                         │
                         ▼
                RAG Recommendations
                
🗄️ Database Architecture
The Version 1 database contains the following main entities:
┌──────────────┐
│   resumes    │
├──────────────┤
│ id           │
│ filename     │
│ extracted_text
│ cleaned_text │
│ skills       │
└──────┬───────┘
       │
       │
       ▼
┌──────────────────┐
│  match_results   │
├──────────────────┤
│ id               │
│ resume_id        │
│ job_id           │
│ matched_skills   │
│ missing_skills   │
│ extra_skills     │
│ skill_match_%    │
│ similarity_%     │
│ final_score      │
└────────┬─────────┘
         │
         │
         ▼
┌──────────────┐
│     jobs     │
├──────────────┤
│ id           │
│ description  │
│ cleaned_text │
│ skills       │
└──────────────┘

┌────────────────────┐
│ knowledge_chunks   │
├────────────────────┤
│ id                 │
│ skill              │
│ title              │
│ content            │
│ level              │
│ embedding          │
└────────────────────┘

⚙️ Installation
1. Clone the Repository
git clone <your-github-repository-url>
cd Ai_Job_Match_Platform

2. Create Virtual Environment
python3 -m venv .venv
Activate:
macOS / Linux
source .venv/bin/activate
Windows
.venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
🐘 PostgreSQL Setup
Create a PostgreSQL database:
ai_job_match_db
Then configure your .env file:
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/ai_job_match_db
Make sure PostgreSQL is running before starting the application.

🔐 Environment Variables
Create a .env file in the project root:
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/ai_job_match_db
Do not commit .env to GitHub.
Use .env.example as a template.

▶️ Run the Application
Activate the virtual environment:
source .venv/bin/activate
Start FastAPI:  uvicorn app.main:app --reloa
The API will be available at:
http://127.0.0.1:8000

📚 API Documentation
FastAPI automatically provides Swagger documentation.
Open:
http://127.0.0.1:8000/docs
Alternative OpenAPI documentation:
http://127.0.0.1:8000/redoc

🔌 Main API Capabilities
The project currently provides API functionality for:
Resume > POST /api/v1/resume/upload
Upload and process a resume PDF.

Job Analysis > POST /api/v1/jobs/analyze
Analyze a job description and extract skills.

Skill Matching > POST /api/v1/matching/skills
Compare resume skills against job skills.

End-to-End Matching > POST /api/v1/matching/match
Match an existing resume with an existing job using database IDs.
Example:
{
  "resume_id": 1,
  "job_id": 1
}
Final Score
POST /api/v1/scoring/final-score
Calculate the weighted final match score.
Example:
{
  "skill_match_percentage": 66.67,
  "text_similarity_percentage": 64.24
}
RAG Recommendations
GET /api/v1/rag/recommendations/{match_result_id}
Generate learning recommendations based on missing skills.
Check the Swagger documentation at /docs for the current complete API routes, request schemas, and response schemas.

🧪 Testing
The project includes a testing stage using:
pytest
httpx

The testing roadmap includes:
Unit tests
API tests
Endpoint validation
Error handling tests
End-to-end workflow testing

Example command:
pytest

Example End-to-End Flow
Step 1 — Upload Resume
Resume PDF
     ↓
PDF Text Extraction
     ↓
Skill Extraction
     ↓
PostgreSQL

Step 2 — Analyze Job
Job Description
     ↓
NLP Processing
     ↓
Skill Extraction
     ↓
PostgreSQL

Step 3 — Match
Resume ID + Job ID
        ↓
Skill Matching
        ↓
TF-IDF Similarity
        ↓
Weighted Score
        ↓
Match Result

Step 4 — Recommendation
Missing Skills
      ↓
Query Embedding
      ↓
pgvector Search
      ↓
Relevant Knowledge
      ↓
Learning Recommendation

📊 Example Result
Example matching result:
{
  "message": "Match result created successfully",
  "match_result_id": 1,
  "resume_id": 1,
  "job_id": 1,
  "matched_skills": [
    "docker",
    "fastapi",
    "machine learning",
    "postgresql",
    "python",
    "scikit-learn"
  ],
  "missing_skills": [
    "aws",
    "natural language processing",
    "rag"
  ],
  "skill_match_percentage": 66.67,
  "similarity_score": 0.6424,
  "text_similarity_percentage": 64.24,
  "skill_weight": 0.7,
  "similarity_weight": 0.3,
  "final_match_score": 65.94
}

🧩 Engineering Concepts Demonstrated
This project demonstrates practical implementation of:
REST API development
FastAPI dependency injection
Pydantic validation
File upload handling
PDF text extraction
NLP preprocessing
Skill extraction
Set-based skill matching
TF-IDF vectorization
Cosine similarity
Weighted scoring
SQLAlchemy ORM
PostgreSQL persistence
JSONB storage
Sentence embeddings
Vector databases
pgvector similarity search
RAG retrieval pipeline
API error handling
End-to-end AI workflow

🏗️ Version 1 Scope
This repository represents Version 1 of the project.
Version 1 — AI Matching Engine
Resume
   +
Job Description
   ↓
NLP
   ↓
Skill Matching
   ↓
TF-IDF
   ↓
Cosine Similarity
   ↓
Weighted Match Score
   ↓
Skill Gap
   ↓
Vector Search
   ↓
Career Recommendations
The main objective of Version 1 is to build and demonstrate the core AI matching engine.

🔮 Version 2 — Recruitment Intelligence
Version 2 is planned as an extension of the Version 1 AI engine.
Potential Version 2 features include:
Job Opening Management
Job Opening Title
Opening Date
Closing Date
Open / Closed Status
Candidate Applications
Multiple Candidate Matching
Bulk Candidate Analysis
Candidate Ranking
Recruitment Insights
HR System Integration
Recruitment Workflow APIs

The Version 2 goal is to integrate the existing AI matching engine into a more realistic recruitment workflow.
🎯 Future Improvements
Potential future improvements include:
Advanced NLP skill extraction
Named Entity Recognition
Improved semantic matching
Better skill normalization
More comprehensive career knowledge base
LLM-based recommendation generation
Authentication and authorization
Background task processing
Docker deployment
CI/CD pipeline
Production deployment
Monitoring and logging
HR system integration
Recruitment dashboard

⚠️ Current Limitations
The current Version 1 implementation is primarily focused on the AI matching engine.
It does not yet provide:
Full HR recruitment workflow
Job application management
Automatic recruitment deadline handling
Candidate ranking dashboard
Production authentication
Full production deployment
External HR system integration

These are planned for future versions.
📌 Project Goals
The main goals of this project are to demonstrate practical AI Engineering skills across:
Machine Learning
       +
NLP
       +
Embeddings
       +
Vector Search
       +
RAG
       +
FastAPI
       +
PostgreSQL
       +
SQLAlchemy

The project is designed as an end-to-end portfolio project rather than a standalone Machine Learning notebook.

👨‍💻 Author
Bhone Thant Zaw
AI Engineer Portfolio Project
Focus Areas: Python, Machine Learning, Scikit-learn, NLP, PyTorch, RAG, FastAPI, PostgreSQL, Vector Search