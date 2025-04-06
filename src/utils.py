from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import sqlite3
from src.config import DB_PATH, MATCH_THRESHOLD
# from src.db import get_all_candidates, update_match_score  # ✅ Add this line
from src.db import get_all_resumes, update_match_score  # ✅ Add this line


def calculate_similarity(candidate_skills, jd_skills):
    """
    Calculates the similarity between two text inputs using TF-IDF and cosine similarity.
    
    :param text1: First text (e.g., candidate skills, experience)
    :param text2: Second text (e.g., job description skills)
    :return: Similarity score between 0 and 1
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([candidate_skills, jd_skills])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity
