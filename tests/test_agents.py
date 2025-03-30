# from src.db import init_db, add_candidate, get_all_candidates
# from src.agents import shortlist_candidates


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.db import init_db, add_candidate, get_all_candidates
from src.agents import shortlist_candidates


def test_agent():
    print("\n📌 Initializing Database...")
    init_db()

    # Sample candidates (Name, Skills, Experience in years)
    candidates = [
        ("Alice Johnson", ["Python", "SQL", "Machine Learning"], 3),
        ("Bob Smith", ["Java", "Spring Boot", "SQL"], 5),
        ("Charlie Brown", ["Python", "Deep Learning", "NLP"], 2),
        ("David Lee", ["JavaScript", "React", "Node.js"], 4),
        ("Eva Green", ["SQL", "Data Analysis", "Power BI"], 6),
    ]

    # Insert sample candidates into the database
    print("\n📌 Adding Sample Candidates...")
    for name, skills, experience in candidates:
        add_candidate(name, skills, experience)
        print(f"✅ Added: {name} | Skills: {skills} | Experience: {experience} years")

    # Fetch all candidates from the database
    print("\n📌 Fetching All Candidates...")
    all_candidates = get_all_candidates()
    for candidate in all_candidates:
        print(candidate)

    # Define a sample JD
    jd_skills = ["Python", "Machine Learning", "SQL"]  # Example JD skills

    # Run the matching agent
    print("\n📌 Running the Matching Agent...")
    shortlisted = shortlist_candidates(jd_skills)

    print("\n🎯 Shortlisted Candidates:")
    for candidate in shortlisted:
        print(f"✅ {candidate[1]} shortlisted with {candidate[2]}% match")

if __name__ == "__main__":
    test_agent()
