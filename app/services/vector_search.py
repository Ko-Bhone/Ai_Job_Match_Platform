from sqlalchemy.orm import Session
from app.models.knowledge import KnowledgeChunk

def search_similar_chunks(db: Session, query_embedding: list[float],
                          top_k: int=3) -> list[KnowledgeChunk]:
    result = (db.query(KnowledgeChunk).
              order_by(KnowledgeChunk.embedding.
                       cosine_distance(query_embedding)).
              limit(top_k).all())

    return result