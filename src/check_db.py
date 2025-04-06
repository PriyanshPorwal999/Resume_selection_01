# from src.db import get_all_candidates

# candidates = get_all_candidates()
# for i, candidate in enumerate(candidates, 1):
#     print(f"\n📄 Candidate {i}")
#     print(f"ID: {candidate['candidate_id']}")
#     print(f"Name: {candidate['name']}")
#     print(f"Email: {candidate['email']}")
#     print(f"Skills: {candidate['skills']}")
#     print(f"Experience: {candidate['experience']}")
#     print(f"Education: {candidate['education']}")
#     print("-" * 40)

# print("📢 Running check_db.py...")




# from src.db import get_all_resumes

# print("📢 Running check_db.py...")

# try:
#     candidates = get_all_resumes()
#     print(f"🔍 Total candidates fetched: {len(candidates)}")

#     if not candidates:
#         print("❌ No candidates found in the database.")
#     else:
#         for i, candidate in enumerate(candidates, 1):
#             print(f"\n📄 Candidate {i}")
#             print(f"ID: {candidate['candidate_id']}")
#             print(f"Name: {candidate['name']}")
#             print(f"Email: {candidate['email']}")
#             print(f"Skills: {candidate['skills']}")
#             print(f"Experience: {candidate['experience']}")
#             print(f"Education: {candidate['education']}")
#             print("-" * 40)

# except Exception as e:
#     print(f"❌ Error fetching candidates: {e}")




from src.db import get_all_resumes

print("📢 Running check_db.py...")

try:
    resumes = get_all_resumes()
    print(f"🔍 Total resumes fetched: {len(resumes)}")

    if not resumes:
        print("❌ No resumes found in the database.")
    else:
        for i, r in enumerate(resumes, 1):
            print(f"\n📄 Candidate {i}")
            print(f"ID: {r['id']}")
            print(f"Name: {r['name']}")
            print(f"Email: {r['email']}")
            print(f"Phone: {r['phone']}")
            print(f"Skills: {r['skills']}")
            print(f"Experience: {r['experience']}")
            print(f"Education: {r['education']}")
            print(f"Certifications: {r['certifications']}")
            print(f"Achievements: {r['achievements']}")
            print(f"Tech Stack: {r['tech_stack']}")
            print("-" * 40)

except Exception as e:
    print(f"❌ Error fetching resumes: {e}")

