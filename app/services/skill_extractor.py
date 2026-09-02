import json
import re
from pathlib import Path

SKILLS_LIFE = Path("data/skills.json")

def load_skills() -> dict:
    with SKILLS_LIFE.open("r", encoding="utf-8") as f:
        data = json.load(f)
        return data["skills"]

def extract_skills(text: str) -> list[str]:
    skills = load_skills()
    found_skills = []
    for canonical_skill, aliases in skills.items():
        for alias in aliases:
            pattern = r"\b" + re.escape(alias.lower()) + r"\b"
            if re.search(pattern, text.lower()):
                found_skills.append(canonical_skill)
                break
    return found_skills
