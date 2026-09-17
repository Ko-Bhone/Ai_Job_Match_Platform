import json
from pathlib import Path

KNOWLEDGE_BASE_PATH = (Path(__file__).resolve().parents[2]/"data"/"career_knowledge.json")

def load_knowledge() -> list[dict]:
    with open(
        KNOWLEDGE_BASE_PATH, "r", encoding="utf-8"
    ) as file:
        knowledge = json.load(file)
    return knowledge