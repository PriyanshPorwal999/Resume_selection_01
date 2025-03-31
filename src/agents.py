# src/agents.py
# import sqlite3
# from src.config import DB_PATH, MATCH_THRESHOLD

# def calculate_match_score(candidate_skills, jd_skills):
#     common_skills = set(candidate_skills).intersection(set(jd_skills))
#     return (len(common_skills) / len(jd_skills)) * 100


# from src.db import get_all_candidates, update_match_score



# def shortlist_candidates(jd_skills):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name, skills FROM candidates")
#     candidates = cursor.fetchall()
#     shortlisted = []
    
#     for candidate in candidates:
#         skills = candidate[2].split(', ')
#         score = calculate_match_score(skills, jd_skills)
#         if score >= MATCH_THRESHOLD:
#             shortlisted.append((candidate[0], candidate[1], score))
    
#     conn.close()
#     return shortlisted



# def shortlist_candidates(jd_skills):
#     """Matches candidates against JD skills and prints shortlisted ones."""
#     candidates = get_all_candidates()
#     shortlisted = []

#     for candidate in candidates:
#         candidate_id, name, skills, experience, match_score = candidate
#         skills_list = eval(skills)  # Convert string back to list

#         # Calculate match percentage
#         match_count = sum(1 for skill in jd_skills if skill in skills_list)
#         match_percentage = (match_count / len(jd_skills)) * 100

#         if match_percentage >= 50:  # Shortlisting threshold
#             update_match_score(candidate_id, match_percentage)
#             shortlisted.append((candidate_id, name, match_percentage))

#     # Print shortlisted candidates
#     if shortlisted:
#         print("\n🎯 Shortlisted Candidates:")
#         for candidate in shortlisted:
#             print(f"✅ {candidate[1]} - Match: {candidate[2]:.2f}%")
#     else:
#         print("❌ No candidates met the criteria.")

#     return shortlisted




import sqlite3
from src.config import DB_PATH, MATCH_THRESHOLD
from src.db import get_all_candidates, update_match_score  # ✅ Add this line

def calculate_match_score(candidate_skills, jd_skills):
    """Calculate skill match percentage."""
    common_skills = set(candidate_skills).intersection(set(jd_skills))
    return (len(common_skills) / len(jd_skills)) * 100

def shortlist_candidates(jd_skills):
    """Matches candidates against JD skills and prints shortlisted ones."""
    candidates = get_all_candidates()  # ✅ Now it will work
    shortlisted = []

    for candidate in candidates:
        candidate_id, name, skills, experience, match_score = candidate
        skills_list = eval(skills)  # Convert string back to list

        # Calculate match percentage
        match_percentage = calculate_match_score(skills_list, jd_skills)

        if match_percentage >= MATCH_THRESHOLD:  # Using threshold from config
            update_match_score(candidate_id, match_percentage)
            shortlisted.append((candidate_id, name, match_percentage))

    # Print shortlisted candidates
    if shortlisted:
        print("\n🎯 Shortlisted Candidates:")
        for candidate in shortlisted:
            print(f"✅ {candidate[1]} - Match: {candidate[2]:.2f}%")
    else:
        print("❌ No candidates met the criteria.")

    return shortlisted

