# src/db.py

# import sqlite3
# from src.config import DB_PATH

# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
#                         id INTEGER PRIMARY KEY, 
#                         name TEXT, 
#                         skills TEXT, 
#                         experience INTEGER, 
#                         match_score INTEGER
#                     )''')
#     conn.commit()
#     conn.close()


import sqlite3
from src.config import DB_PATH
# from src.config import DB_PATH



import ast

def init_db():
    """Initialize the database and create the candidates table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(DB_PATH)

    cursor.execute("DROP TABLE IF EXISTS candidates")



    # cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
    #                     id INTEGER PRIMARY KEY, 
    #                     name TEXT, 
    #                     skills TEXT, 
    #                     experience INTEGER, 
    #                     match_score INTEGER DEFAULT 0
    #                 )''')
    # conn.commit()

    cursor.execute('''CREATE TABLE candidates (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        skills TEXT, 
                        experience TEXT, 
                        certifications TEXT,
                        match_score REAL DEFAULT 0
                    )''')
    conn.commit()

    conn.close()
    print("🗑️ Old table dropped and new table created with TEXT fields.")
    # print("🗑️ Database reset successfully!")

# def add_candidate(name, skills, experience):
#     """Insert a new candidate into the database."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO candidates (name, skills, experience) VALUES (?, ?, ?)", 
#                    (name, str(skills), experience))
#     conn.commit()
#     conn.close()




# def add_candidate(name, skills, experience):
#     """Insert a new candidate into the database only if they don't already exist."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

    
    
#     # Check if the candidate already exists
#     cursor.execute("SELECT id FROM candidates WHERE name = ?", (name,))
#     existing_candidate = cursor.fetchone()
    
#     if existing_candidate:
#         print(f"⚠️ Candidate {name} already exists in the database. Skipping insertion.")
#         conn.close()
#         return
    
#     cursor.execute("INSERT INTO candidates (name, skills, experience) VALUES (?, ?, ?)", 
#                     (name, str(skills), experience))
#     conn.commit()
#     print(f"✅ Added: {name} | Skills: {skills} | Experience: {experience} years")

#     conn.close()




def add_candidate(name, skills, experience, certifications):
    """Insert a new candidate into the database only if they don't already exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM candidates WHERE name = ?", (name,))
    existing_candidate = cursor.fetchone()

    if existing_candidate:
        print(f"⚠️ Candidate {name} already exists in the database. Skipping insertion.")
        conn.close()
        return

    cursor.execute(
        "INSERT INTO candidates (name, skills, experience, certifications) VALUES (?, ?, ?, ?)", 
        (name, str(skills), str(experience), str(certifications))
    )
    conn.commit()
    print(f"✅ Added: {name} | Skills: {skills} | Experience: {experience} | Certifications: {certifications}")
    conn.close()




# def get_all_candidates():
#     """Retrieve all candidates from the database."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM candidates")
#     candidates = cursor.fetchall()
#     conn.close()
#     return candidates







# def get_all_candidates():
#     """Retrieve all candidates from the database and parse text fields."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM candidates")
#     rows = cursor.fetchall()
#     conn.close()

#     candidates = []
#     for row in rows:
#         candidates.append({
#             "id": row[0],
#             "name": row[1],
#             "skills": ast.literal_eval(row[2]) if row[2] else [],
#             "experience": ast.literal_eval(row[3]) if row[3] else [],
#             "certifications": ast.literal_eval(row[4]) if row[4] else [],
#             "match_score": row[5]
#         })

#     return candidates




# def get_all_resumes():
#     """Retrieve all resumes from the database and parse text fields."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name, skills, experience, certifications FROM resumes")
#     rows = cursor.fetchall()
#     conn.close()

#     resumes = []
#     for row in rows:
#         resumes.append({
#             "id": row[0],
#             "name": row[1],
#             "skills": ast.literal_eval(row[2]) if row[2] else [],
#             "experience": ast.literal_eval(row[3]) if row[3] else [],
#             "certifications": ast.literal_eval(row[4]) if row[4] else []
#         })

#     print(f"📥 Loaded {len(resumes)} resumes from database.")
#     return resumes


def get_all_resumes():
    """Retrieve all resumes from the database and parse fields."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resumes")
    rows = cursor.fetchall()
    conn.close()

    resumes = []
    for row in rows:
        resumes.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "skills": ast.literal_eval(row[4]) if row[4] else [],
            "experience": ast.literal_eval(row[5]) if row[5] else [],
            "education": ast.literal_eval(row[6]) if row[6] else [],
            "certifications": ast.literal_eval(row[7]) if row[7] else [],
            "achievements": ast.literal_eval(row[8]) if row[8] else [],
            "tech_stack": ast.literal_eval(row[9]) if row[9] else [],
        })

    print(f"📥 Loaded {len(resumes)} resumes from database.")
    return resumes







def update_match_score(candidate_id, score):
    """Update the match score of a candidate."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE candidates SET match_score = ? WHERE id = ?", (score, candidate_id))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()