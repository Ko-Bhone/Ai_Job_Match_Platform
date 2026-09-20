from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

def create_embeddings(chunks : list[dict]) -> list[dict]:
    texts = [chunk["content"] for chunk in chunks]
    embeddings = model.encode(texts, convert_to_numpy=True)
    embedded_chunks = []
    for chunk, embedding in zip(chunks, embeddings):
        embedded_chunks.append({**chunk, "embedding": embedding.tolist()})
    return embedded_chunks

def create_query_embedding(text: str) -> list[float]:
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()

