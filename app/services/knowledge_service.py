from sqlalchemy.orm import Session
from app.models.knowledge import KnowledgeChunk

def save_knowledge_chunks(db: Session, embedded_chunk: list[dict]) -> list[KnowledgeChunk]:

    save_chunk = []
    for chunk in embedded_chunk:
        knowledge_chunk = KnowledgeChunk(
            skill = chunk["skill"],
            title = chunk["title"],
            content = chunk["content"],
            level = chunk["level"],
            embedding = chunk["embedding"]
        )
        db.add(knowledge_chunk)
        save_chunk.append(knowledge_chunk)
    db.commit()
    for chunk in save_chunk:
        db.refresh(chunk)
    return save_chunk
