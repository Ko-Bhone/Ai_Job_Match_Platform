from app.services.match_score import calculate_final_match_score

def test_final_match_score():
    result = calculate_final_match_score(
        skill_match_percentage=80,
        text_similarity_percentage=60
    )

    assert result["skill_weight"] == 0.70
    assert result["similarity_weight"] == 0.30
    assert result["weighted_skill_score"] == 56.0
    assert result["weighted_similarity_score"] == 18.0
    assert result["final_match_score"] == 74.0

def test_final_match_score_zero():
    result = calculate_final_match_score(
        skill_match_percentage=0,
        text_similarity_percentage=0
    )
    assert result["final_match_score"] == 0.0

def test_final_match_score_hundred():
    result = calculate_final_match_score(
        skill_match_percentage=100,
        text_similarity_percentage = 100
    )
    assert result["final_match_score"] == 100.0
