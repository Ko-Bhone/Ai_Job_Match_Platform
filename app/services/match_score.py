def calculate_final_match_score(skill_match_percentage: float, text_similarity_percentage: float) -> dict:
    skill_weight = 0.70
    similarity_weight = 0.30
    weight_skill_score = (skill_match_percentage * skill_weight)
    weight_similarity_score = (text_similarity_percentage * similarity_weight)
    final_match_score = (weight_skill_score + weight_similarity_score)
    return {
        "skill_match_percentage": round(skill_match_percentage, 2),
        "text_similarity_percentage": round(text_similarity_percentage, 2),
        "skill_weight": skill_weight,
        "similarity_weight": similarity_weight,
        "weight_skill_score": round(weight_skill_score, 2),
        "weight_similarity_score": round(weight_similarity_score, 2),
        "final_match_score": round(final_match_score, 2)
    }