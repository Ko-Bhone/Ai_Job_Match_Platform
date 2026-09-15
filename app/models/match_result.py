from datetime import datetime
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class MatchResult(Base):
    __tablename__ = "match_results"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resume_id : Mapped[int] = mapped_column(ForeignKey("resumes.id"), nullable=False)
    job_id : Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False)
    matched_skills : Mapped[list | None] = mapped_column(JSONB, nullable=True)
    missing_skills : Mapped[list | None] = mapped_column(JSONB, nullable=True)
    extra_skills : Mapped[list | None] = mapped_column(JSONB, nullable=True)
    skill_match_percentage : Mapped[float | None] = mapped_column(Float, nullable=True)
    text_similarity_percentage : Mapped[float | None] = mapped_column(Float, nullable=True)
    skill_weight : Mapped[float] = mapped_column(Float, default=0.70)
    similarity_weight : Mapped[float] = mapped_column(Float, default=0.30)
    final_match_score : Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at : Mapped[datetime] = mapped_column(DateTime, default = datetime.utcnow())