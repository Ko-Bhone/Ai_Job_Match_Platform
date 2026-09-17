from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_text_similarity(resume_text: str, job_description: str) -> dict:
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    similarity_score = float(similarity_matrix[0][0])
    similarity_percentage = float(similarity_score * 100)
    return {
        "similarity_score": round(similarity_score, 4),
        "similarity_percentage": round(similarity_percentage, 2)}