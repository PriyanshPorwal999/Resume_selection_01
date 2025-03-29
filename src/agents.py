# src/agents.py
import sqlite3
from src.config import DB_PATH, MATCH_THRESHOLD

def calculate_match_score(candidate_skills, jd_skills):
    common_skills = set(candidate_skills).intersection(set(jd_skills))
    return (len(common_skills) / len(jd_skills)) * 100

def shortlist_candidates(jd_skills):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, skills FROM candidates")
    candidates = cursor.fetchall()
    shortlisted = []
    
    for candidate in candidates:
        skills = candidate[2].split(', ')
        score = calculate_match_score(skills, jd_skills)
        if score >= MATCH_THRESHOLD:
            shortlisted.append((candidate[0], candidate[1], score))
    
    conn.close()
    return shortlisted