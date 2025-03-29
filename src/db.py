# src/db.py
import sqlite3
from src.config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        skills TEXT, 
                        experience INTEGER, 
                        match_score INTEGER
                    )''')
    conn.commit()
    conn.close()