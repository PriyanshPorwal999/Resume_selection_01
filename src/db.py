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

def init_db():
    """Initialize the database and create the candidates table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        skills TEXT, 
                        experience INTEGER, 
                        match_score INTEGER DEFAULT 0
                    )''')
    conn.commit()
    conn.close()

def add_candidate(name, skills, experience):
    """Insert a new candidate into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO candidates (name, skills, experience) VALUES (?, ?, ?)", 
                   (name, str(skills), experience))
    conn.commit()
    conn.close()

def get_all_candidates():
    """Retrieve all candidates from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()
    conn.close()
    return candidates

def update_match_score(candidate_id, score):
    """Update the match score of a candidate."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE candidates SET match_score = ? WHERE id = ?", (score, candidate_id))
    conn.commit()
    conn.close()
