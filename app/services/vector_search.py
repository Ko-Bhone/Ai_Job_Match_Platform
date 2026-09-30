from sqlalchemy.orm import Session
from app.models.knowledge import KnowledgeChunk

def search_similar_chunks(db: Session, query_embedding: list[float], skill: str | None = None,
                          top_k: int=3) -> list[KnowledgeChunk]:

    query = db.query(KnowledgeChunk)
    if skill:
        query = query.filter(KnowledgeChunk.skill == skill)
        result = query.filter(KnowledgeChunk.embedding.is_not(None)._order_by
                              (KnowledgeChunk.embedding.cosine_distance(query_embedding)).
                              limit(top_k).all())

    return result