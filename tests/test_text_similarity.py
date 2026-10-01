from app.services.text_similarity import calculate_text_similarity

def test_text_similarity_identical_text():
    text = "Python Fast API machine learning"
    result = calculate_text_similarity(resume_text=text, job_description=text)
    assert result["similarity_score"] == 1.0
    assert result["similarity_percentage"] == 100.0

def test_text_similarity_different_text():
    result = calculate_text_similarity(resume_text= "Python Fast API backend development",
                                       job_description = "Javascript frontend development")

    assert 0.0 <= result["similarity_score"] <= 1.0
    assert 0.0 <= result["similarity_percentage"] <= 100.0

def test_text_similarity_related_text():
    result = calculate_text_similarity(
        resume_text = "Python machine learning with Scikit-learn",
        job_description = "Python developer with machine learning experience"
    )
    assert result["similarity_score"] > 0
    assert result["similarity_percentage"] > 0