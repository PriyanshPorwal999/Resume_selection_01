import json
import sqlite3
# from src.db import get_all_candidates  # Fetches all resumes from the database
from src.db import get_all_resumes  # Fetches all resumes from the database

from src.utils import calculate_similarity  # Utility function for comparing text
import ast  # Add this at the top of matcher.py if not already

import re



# Load Job Summary JSON
def load_job_summary(JOB_SUMMARY_PATH):
    """Loads the job summary JSON file."""
    with open(JOB_SUMMARY_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

# Extract candidate resumes from DB
# def get_candidate_data(DB_PATH):
# def get_candidate_data():
    # """Fetches all candidate resumes from the database."""
    # return get_all_candidates()  # Assume this function returns a list of resumes as dicts





# def get_candidate_data():
    """Fetches all candidate resumes from the database."""
    # raw_candidates = get_all_candidates()

    # raw_candidates = get_all_resumes()


    # candidates = []

    # for row in raw_candidates:
    #     candidates.append({
    #         "id": row[0],
    #         "name": row[1],
    #         "skills": ast.literal_eval(row[2]) if row[2] else [],
    #         "experience": ast.literal_eval(row[3]) if row[3] else [],
    #         "certifications": ast.literal_eval(row[4]) if len(row) > 4 and row[4] else [],
    #     })


    # for row in raw_candidates:
    #     candidates.append({
    #         "id": row[0],
    #         "name": row[1],
    #         "skills": ast.literal_eval(row[2]) if isinstance(row[2], str) and row[2] else [],
    #         "experience": ast.literal_eval(row[3]) if isinstance(row[3], str) and row[3] else [],
    #         "certifications": ast.literal_eval(row[4]) if len(row) > 4 and isinstance(row[4], str) and row[4] else [],
    #     })    

    # print("[DEBUG] Parsed Candidate Example:", candidates[0])
    

    # return candidates



# import ast
# from src.db import get_all_resumes

# def get_candidate_data():
#     """Fetches all candidate resumes from the database and returns a cleaned list."""

#     raw_candidates = get_all_resumes()
#     candidates = []

#     for row in raw_candidates:
#         candidate = {
#             "id": row['id'],
#             "name": row['name'],
#             "skills": ast.literal_eval(row['skills']) if row['skills'] else [],
#             "experience": ast.literal_eval(row['experience']) if row['experience'] else [],
#             "education": ast.literal_eval(row['education']) if row['education'] else [],
#             "certifications": ast.literal_eval(row['certifications']) if row['certifications'] else [],
#             "tech_stack": ast.literal_eval(row['tech_stack']) if row['tech_stack'] else []
#         }
#         candidates.append(candidate)

#     # Optional: Preview first candidate
#     if candidates:
#         print("[DEBUG] Parsed Candidate Example:", candidates[0])
#     else:
#         print("[DEBUG] No candidates found.")

#     return candidates




def get_candidate_data():
    raw_candidates = get_all_resumes()
    candidates = []

    for row in raw_candidates:
        candidate = {
            "id": row['id'],
            "name": row['name'],
            "skills": row['skills'],
            "experience": row['experience'],
            "education": row['education'],
            "certifications": row['certifications'],
            "achievements": row['achievements'],
            "tech_stack": row['tech_stack']
        }
        candidates.append(candidate)

    if candidates:
        print("[DEBUG] Parsed Candidate Example:", candidates[0])
    return candidates








# Compare candidate with job summary
# def match_candidates(jd_skills, candidate_skills):
#     """Compares each candidate's skills, experience, and certifications with the job summary."""
#     shortlisted = []

#     # required_skills = set(jd_skills["skills"])  # Skills required for the job
#     required_skills = set(jd_skills.get("skills", []))
#     required_experience = set(jd_skills.get("experience", []))
#     required_certifications = set(jd_skills.get("certifications", []))

#     for candidate in candidate_skills:
#         candidate_skills = set(candidate["skills"])
#         candidate_experience = set(exp["job_title"] for exp in candidate.get("experience", []))
#         candidate_certifications = set(candidate.get("certifications", []))

#         # Calculate matches
#         skill_match = len(required_skills & candidate_skills) / max(len(required_skills), 1)
#         experience_match = len(required_experience & candidate_experience) / max(len(required_experience), 1)
#         cert_match = len(required_certifications & candidate_certifications) / max(len(required_certifications), 1)

#         print(f"[DEBUG] Candidate: {candidate['name']} | Skill Match: {skill_match:.2f} | Experience Match: {experience_match:.2f} | Certification Match: {cert_match:.2f}")

#         # Weighted scoring
#         # total_score = (0.5 * skill_match) + (0.3 * experience_match) + (0.2 * cert_match)

#         total_score = ((0.5 * skill_match) + (0.3 * experience_match) + (0.2 * cert_match))*100


    #     if total_score > 0:  # Only shortlist candidate_skills with non-zero match score
    #         shortlisted.append({"candidate_id": candidate["id"], "name": candidate["name"], "score": total_score})

    # # Sort by highest match score
    # shortlisted.sort(key=lambda x: x["score"], reverse=True)
    # return shortlisted

# Main function to run matching
# def run_matching(DB_PATH, JOB_SUMMARY_PATH):
#     """Executes the candidate matching process."""
#     print("[INFO] Loading job summary...")
#     jd_skills = load_job_summary(JOB_SUMMARY_PATH)

#     # ✅ Fix: If job summary is a list, use the first item
#     if isinstance(jd_skills, list):
#         jd_skills = jd_skills[0]

#     # print("[DEBUG] Job Summary Data:", jd_skills)



#     print("[INFO] Fetching candidate_skills from database...")
#     # candidate_skills = get_candidate_data(DB_PATH)
#     candidate_skills = get_candidate_data()

#     # print("[DEBUG] Job Summary Data:", candidate_skills)


#     print("[INFO] Matching candidate_skills...")
#     shortlisted_candidates = match_candidates(jd_skills, candidate_skills)

#     print("\n🎯 Shortlisted Candidates:")
#     for idx, candidate in enumerate(shortlisted_candidates, start=1):
#         print(f"{idx}. {candidate['name']} (Match Score: {candidate['score']:.2f})")

#     return shortlisted_candidates

# Run if executed directly
# if __name__ == "__main__":
#     DB_PATH = "resume_selection.sqlite3"
#     JOB_SUMMARY_PATH = r"D:\OneDrive\Desktop\Resume_Selection\job_summaries03.json"
#     run_matching(DB_PATH, JOB_SUMMARY_PATH)





def run_matching(DB_PATH, JOB_SUMMARY_PATH):
    print("[INFO] Loading job summary...")
    jd_skills = load_job_summary(JOB_SUMMARY_PATH)



    # ✅ Use this here
    if isinstance(jd_skills, list):
        jd_skills = jd_skills[0]

    print("[DEBUG] Job Summary Data:", jd_skills)    

    print("[INFO] Fetching candidate data from database...")
    # candidate_skills = get_candidate_data(DB_PATH)
    candidate_skills = get_candidate_data()


    print("[DEBUG] Job Summary Data:", candidate_skills)


    print("[INFO] Matching candidates...")
    shortlisted_candidates = match_candidates(jd_skills, candidate_skills)

    print("\n🎯 Shortlisted Candidates:")
    for idx, candidate in enumerate(shortlisted_candidates, start=1):
        print(f"{idx}. {candidate['name']} (Match Score: {candidate['score']:.2f})")

    return shortlisted_candidates





# import re

def clean_and_tokenize(text):
    """Cleans and tokenizes input text."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove punctuation
    return set(text.split())

def match_candidates(jd_skills, candidate_skills):
    """Compares each candidate's skills, experience, and certifications with the job summary."""
    shortlisted = []

    # Clean and flatten job description data
    required_skills = set()
    for skill in jd_skills.get("skills", []):
        required_skills |= clean_and_tokenize(skill)

    required_experience = set()
    for exp in jd_skills.get("experience", []):
        required_experience |= clean_and_tokenize(exp)

    required_certifications = set()
    for cert in jd_skills.get("certifications", []):
        required_certifications |= clean_and_tokenize(cert)

    for candidate in candidate_skills:
        candidate_skill_tokens = set()
        for skill in candidate.get("skills", []):
            candidate_skill_tokens |= clean_and_tokenize(skill)

        candidate_experience_tokens = set()
        for exp in candidate.get("experience", []):
            candidate_experience_tokens |= clean_and_tokenize(exp.get("job_title", ""))

        candidate_cert_tokens = set()
        for cert in candidate.get("certifications", []):
            candidate_cert_tokens |= clean_and_tokenize(cert)

        # Calculate matches
        skill_match = len(required_skills & candidate_skill_tokens) / max(len(required_skills), 1)
        experience_match = len(required_experience & candidate_experience_tokens) / max(len(required_experience), 1)
        cert_match = len(required_certifications & candidate_cert_tokens) / max(len(required_certifications), 1)

        print(f"[DEBUG] Candidate: {candidate['name']} | Skill Match: {skill_match:.2f} | Experience Match: {experience_match:.2f} | Certification Match: {cert_match:.2f}")

        # Weighted scoring
        total_score = ((0.5 * skill_match) + (0.3 * experience_match) + (0.2 * cert_match)) * 100

        if total_score > 0:
            shortlisted.append({"candidate_id": candidate["id"], "name": candidate["name"], "score": total_score})

    # Sort by highest match score
    shortlisted.sort(key=lambda x: x["score"], reverse=True)
    return shortlisted


# Run if executed directly
if __name__ == "__main__":
    DB_PATH = "resume_selection.sqlite3"
    JOB_SUMMARY_PATH = r"D:\OneDrive\Desktop\Resume_Selection\job_summaries03.json"
    run_matching(DB_PATH, JOB_SUMMARY_PATH)
    # match_candidates(DB_PATH, JOB_SUMMARY_PATH)




# old
# jd_skills, candidate_skills

# new
# candidate_skills, jd_skills



# Old
# DB_PATH, JOB_SUMMARY_PATH


# old
# json_path