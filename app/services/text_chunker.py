
def create_chunks(knowledge: list[dict], chunk_size: int=200) -> list[dict]:
    chunks = []
    for item in knowledge:
        content = item["content"]
        words = content.split()
        for i in range(0, len(words), chunk_size):
            chunk_text = " ".join(words[i:i + chunk_size])
            chunks.append({
                "skill": item["skill"],
                "title": item["title"],
                "content": chunk_text,
                "level": item["level"]
            })
    return chunks