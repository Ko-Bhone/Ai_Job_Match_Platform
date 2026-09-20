from datetime import datetime
from sqlalchemy import String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector
from app.database.base import Base

class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    skill: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    level: Mapped[str | None] = mapped_column(String(50), nullable=True)
    embedding: Mapped[list | None] = mapped_column(Vector(384), nullable=True)
    chunk_metadata: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)