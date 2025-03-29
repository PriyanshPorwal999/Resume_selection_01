# src/main.py
from src.db import init_db
from src.agents import shortlist_candidates


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.db import init_db
from src.agents import shortlist_candidates


def main():
    init_db()
    jd_skills = ["Python", "Machine Learning", "SQL"]  # Example JD skills
    shortlisted = shortlist_candidates(jd_skills)
    for candidate in shortlisted:
        print(f"Candidate {candidate[1]} shortlisted with {candidate[2]}% match")

if __name__ == "__main__":
    main()