# import pdfplumber
# import json
# import sqlite3
# import os
# from src.config import DB_PATH

# # Newly added content start
# import sys
# import os

# # Add the project root directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from src.config import DB_PATH  # Now it should work!

# # Newly added content end


# def extract_text_from_pdf(pdf_path):
#     """Extract text from a given PDF file."""
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text

# def parse_resume_to_json(text):
#     """Parse resume text into a structured JSON format."""
#     lines = text.split('\n')
    
#     resume_json = {
#         "candidate_id": lines[0].split(":")[-1].strip() if "ID:" in lines[0] else "Unknown",
#         "name": lines[1].split(":")[-1].strip() if "Name:" in lines[1] else "Unknown",
#         "email": lines[2].split(":")[-1].strip() if "Email:" in lines[2] else "Unknown",
#         "phone": lines[3].split(":")[-1].strip() if "Phone:" in lines[3] else "Unknown",
#         "education": [],
#         "experience": [],
#         "skills": [],
#         "certifications": [],
#         "achievements": [],
#         "tech_stack": []
#     }
    
#     for i, line in enumerate(lines):
#         if "Education" in line:
#             resume_json["education"].append({
#                 "degree": lines[i+1].strip(),
#                 "years": lines[i+2].strip(),
#                 "details": lines[i+3].strip()
#             })
#         elif "Work Experience" in line:
#             resume_json["experience"].append({
#                 "job_title": lines[i+1].split(" at ")[0].strip(),
#                 "company": lines[i+1].split(" at ")[-1].strip(),
#                 "years": lines[i+2].strip(),
#                 "details": lines[i+3].strip()
#             })
#         elif "Skills" in line:
#             resume_json["skills"] = [s.strip() for s in lines[i+1].split(" - ")[-1].split(",")]
#         elif "Certifications" in line:
#             resume_json["certifications"].append(lines[i+1].strip())
#         elif "Achievements" in line:
#             resume_json["achievements"].append(lines[i+1].strip())
#         elif "Tech Stack" in line:
#             resume_json["tech_stack"] = [s.strip() for s in lines[i+1].split(",")]
    
#     return resume_json

# def store_resume_in_db(resume_json):
#     """Store extracted resume data into SQLite database."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
    
#     cursor.execute('''CREATE TABLE IF NOT EXISTS resumes (
#                         id TEXT PRIMARY KEY,
#                         name TEXT,
#                         email TEXT,
#                         phone TEXT,
#                         skills TEXT,
#                         experience TEXT,
#                         education TEXT,
#                         certifications TEXT,
#                         achievements TEXT,
#                         tech_stack TEXT
#                     )''')
    
#     cursor.execute("""
#         INSERT INTO resumes (id, name, email, phone, skills, experience, education, certifications, achievements, tech_stack)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#         (
#             resume_json["candidate_id"],
#             resume_json["name"],
#             resume_json["email"],
#             resume_json["phone"],
#             json.dumps(resume_json["skills"]),
#             json.dumps(resume_json["experience"]),
#             json.dumps(resume_json["education"]),
#             json.dumps(resume_json["certifications"]),
#             json.dumps(resume_json["achievements"]),
#             json.dumps(resume_json["tech_stack"])
#         )
#     )
    
#     conn.commit()
#     conn.close()
#     print(f"✅ Resume for {resume_json['name']} stored successfully!")

# # Example usage:
# if __name__ == "__main__":
#     pdf_path = r"D:\OneDrive\Desktop\Hackathon_material\Dataset (1)\Dataset\[Usecase 5] AI-Powered Job Application Screening System\CVs1\C1061.pdf"  # Replace with actual PDF path
#     text = extract_text_from_pdf(pdf_path)
#     resume_json = parse_resume_to_json(text)
#     store_resume_in_db(resume_json)



import pdfplumber
import json
import sqlite3
import os
import sys
from src.config import DB_PATH

# Ensure the src module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
    except Exception as e:
        print(f"❌ Error extracting text from {pdf_path}: {e}")
    return text.strip()

# def parse_resume_to_json(text):
#     """Parse resume text into a structured JSON format."""
#     lines = text.split('\n')
    
#     resume_json = {
#         "candidate_id": "Unknown",
#         "name": "Unknown",
#         "email": "Unknown",
#         "phone": "Unknown",
#         "education": [],
#         "experience": [],
#         "skills": [],
#         "certifications": [],
#         "achievements": [],
#         "tech_stack": []
#     }

#     for i, line in enumerate(lines):
#         if line.lower().startswith("id:"):
#             resume_json["candidate_id"] = line.split(":")[-1].strip()
#         elif line.lower().startswith("name:"):
#             resume_json["name"] = line.split(":")[-1].strip()
#         elif line.lower().startswith("email:"):
#             resume_json["email"] = line.split(":")[-1].strip()
#         elif line.lower().startswith("phone:"):
#             resume_json["phone"] = line.split(":")[-1].strip()
#         elif "education" in line.lower():
#             if i + 3 < len(lines):
#                 resume_json["education"].append({
#                     "degree": lines[i+1].strip(),
#                     "years": lines[i+2].strip(),
#                     "details": lines[i+3].strip()
#                 })
#         elif "work experience" in line.lower():
#             if i + 3 < len(lines):
#                 resume_json["experience"].append({
#                     "job_title": lines[i+1].split(" at ")[0].strip(),
#                     "company": lines[i+1].split(" at ")[-1].strip(),
#                     "years": lines[i+2].strip(),
#                     "details": lines[i+3].strip()
#                 })
#         elif "skills" in line.lower():
#             resume_json["skills"] = [s.strip() for s in lines[i+1].split(",") if s.strip()]
#         elif "certifications" in line.lower():
#             resume_json["certifications"].append(lines[i+1].strip())
#         elif "achievements" in line.lower():
#             resume_json["achievements"].append(lines[i+1].strip())
#         elif "tech stack" in line.lower():
#             resume_json["tech_stack"] = [s.strip() for s in lines[i+1].split(",") if s.strip()]

#     return resume_json



import hashlib

def parse_resume_to_json(text):
    """Parse resume text into a structured JSON format."""
    lines = text.split('\n')

    # Extract candidate ID, Name, Email, and Phone
    candidate_id = None
    name, email, phone = "Unknown", "Unknown", "Unknown"

    for line in lines:
        if "ID:" in line:
            candidate_id = line.split(":")[-1].strip()
        elif "Name:" in line:
            name = line.split(":")[-1].strip()
        elif "Email:" in line:
            email = line.split(":")[-1].strip()
        elif "Phone:" in line:
            phone = line.split(":")[-1].strip()

    # If candidate_id is missing, generate it using a hash of email
    if not candidate_id or candidate_id == "Unknown":
        candidate_id = hashlib.md5(email.encode()).hexdigest()[:8]  # Generate short unique ID

    resume_json = {
        "candidate_id": candidate_id,
        "name": name,
        "email": email,
        "phone": phone,
        "education": [],
        "experience": [],
        "skills": [],
        "certifications": [],
        "achievements": [],
        "tech_stack": []
    }

    # Extract structured data
    for i, line in enumerate(lines):
        if "Education" in line:
            resume_json["education"].append({
                "degree": lines[i+1].strip() if i+1 < len(lines) else "",
                "years": lines[i+2].strip() if i+2 < len(lines) else "",
                "details": lines[i+3].strip() if i+3 < len(lines) else ""
            })
        elif "Work Experience" in line:
            resume_json["experience"].append({
                "job_title": lines[i+1].split(" at ")[0].strip() if " at " in lines[i+1] else lines[i+1].strip(),
                "company": lines[i+1].split(" at ")[-1].strip() if " at " in lines[i+1] else "Unknown",
                "years": lines[i+2].strip() if i+2 < len(lines) else "",
                "details": lines[i+3].strip() if i+3 < len(lines) else ""
            })
        elif "Skills" in line:
            resume_json["skills"] = [s.strip() for s in lines[i+1].split(",")]
        elif "Certifications" in line:
            resume_json["certifications"].append(lines[i+1].strip())
        elif "Achievements" in line:
            resume_json["achievements"].append(lines[i+1].strip())
        elif "Tech Stack" in line:
            resume_json["tech_stack"] = [s.strip() for s in lines[i+1].split(",")]

    return resume_json





# def store_resume_in_db(resume_json):
#     """Store extracted resume data into SQLite database, avoiding duplicates."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS resumes (
#                         id TEXT PRIMARY KEY,
#                         name TEXT,
#                         email TEXT,
#                         phone TEXT,
#                         skills TEXT,
#                         experience TEXT,
#                         education TEXT,
#                         certifications TEXT,
#                         achievements TEXT,
#                         tech_stack TEXT
#                     )''')

#     # Check if candidate already exists
#     cursor.execute("SELECT id FROM resumes WHERE id = ?", (resume_json["candidate_id"],))
#     existing_candidate = cursor.fetchone()
    
#     if existing_candidate:
#         print(f"⚠️ Resume for {resume_json['name']} already exists in the database. Skipping.")
#     else:
#         cursor.execute("""
#             INSERT INTO resumes (id, name, email, phone, skills, experience, education, certifications, achievements, tech_stack)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#             (
#                 resume_json["candidate_id"],
#                 resume_json["name"],
#                 resume_json["email"],
#                 resume_json["phone"],
#                 json.dumps(resume_json["skills"]),
#                 json.dumps(resume_json["experience"]),
#                 json.dumps(resume_json["education"]),
#                 json.dumps(resume_json["certifications"]),
#                 json.dumps(resume_json["achievements"]),
#                 json.dumps(resume_json["tech_stack"])
#             )
#         )
#         conn.commit()
#         print(f"✅ Resume for {resume_json['name']} stored successfully!")

#     conn.close()



def store_resume_in_db(resume_json):
    """Store extracted resume data into SQLite database while checking for duplicates."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS resumes (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        skills TEXT,
                        experience TEXT,
                        education TEXT,
                        certifications TEXT,
                        achievements TEXT,
                        tech_stack TEXT
                    )''')
    
    # Check if the candidate already exists in the database
    cursor.execute("SELECT id FROM resumes WHERE id = ?", (resume_json["candidate_id"],))
    existing_entry = cursor.fetchone()

    if existing_entry:
        print(f"⚠️ Resume for {resume_json['name']} already exists in the database. Skipping.")
    else:
        cursor.execute("""
            INSERT INTO resumes (id, name, email, phone, skills, experience, education, certifications, achievements, tech_stack)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                resume_json["candidate_id"],
                resume_json["name"],
                resume_json["email"],
                resume_json["phone"],
                json.dumps(resume_json["skills"]),
                json.dumps(resume_json["experience"]),
                json.dumps(resume_json["education"]),
                json.dumps(resume_json["certifications"]),
                json.dumps(resume_json["achievements"]),
                json.dumps(resume_json["tech_stack"])
            )
        )
        conn.commit()
        print(f"✅ Resume for {resume_json['name']} stored successfully!")

    conn.close()





def process_resumes_from_folder(folder_path):
    """Process all PDFs in the given folder and store them in the database."""
    if not os.path.exists(folder_path):
        print(f"❌ Folder {folder_path} does not exist.")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("⚠️ No PDF resumes found in the folder.")
        return

    print(f"📂 Found {len(pdf_files)} resumes. Processing...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        
        if text:
            resume_json = parse_resume_to_json(text)
            store_resume_in_db(resume_json)
        else:
            print(f"⚠️ No text found in {pdf_file}. Skipping.")

if __name__ == "__main__":
    # Set the folder containing resume PDFs
    resumes_folder = r"D:\OneDrive\Desktop\Hackathon_material\CVs1"  # Replace with your actual path

    process_resumes_from_folder(resumes_folder)

