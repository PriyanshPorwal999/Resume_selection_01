import streamlit as st
import pandas as pd
import json

import PyPDF2
# import os


st.set_page_config(page_title="AI Resume Screening", layout="centered")

# Title
st.title("🤖 Enhancing Job Screening with AI & Data Intelligence")

# Project Overview
with st.expander("📌 Project Overview"):
    st.markdown("""
    This project uses **multi-agent AI** to automate resume screening:
    
    1. 📄 **Summarizes Job Descriptions**
    2. 🧠 **Compares candidate skills from database**
    3. ✅ **Shortlists matching candidates**
    4. ✉️ **Sends interview invites automatically**
    
    Built using: **Python, Streamlit, SQLite, Multi-Agent AI Framework**
    """)

# Upload Job Description
st.subheader("📄 Upload Job Description")
jd_file = st.file_uploader("Upload a csv file containing the Job Description", type=["csv"])



if jd_file:
    st.success("Job Description uploaded successfully!")
    # Dummy placeholder summary (you'll replace this with your model output)
    st.subheader("🧠 Summarized Job Description")
    st.json({
        "Title": "Software Engineer Intern",
        "Key Skills": ["Python", "Machine Learning", "SQL", "Communication"],
        "Experience": "0-1 Years",
        "Location": "Remote"
    })

# Upload Candidate Database
# st.subheader("👨‍💼 Upload Candidate Data (Txt, Pdf)")
# db_file = st.file_uploader("Upload candidate data file", type=["txt", "pdf"])

# if db_file:
#     candidates_df = pd.read_csv(db_file)
#     st.success("Candidate data uploaded successfully!")
#     st.dataframe(candidates_df)

#     # Dummy logic for shortlisted candidates (replace with actual comparison logic)
#     st.subheader("✅ Shortlisted Candidates (Mock Output)")
#     shortlisted_df = candidates_df.head(3)  # Mock top 3
#     st.dataframe(shortlisted_df)

#     if st.button("📤 Send Interview Invites"):
#         st.success("Invites sent to shortlisted candidates!")



# import PyPDF2

# st.subheader("👨‍💼 Upload Candidate Data (.csv for now)")

# db_file = st.file_uploader("Upload candidate data file", type=["csv", "txt", "pdf"])

# if db_file:
#     file_name = db_file.name.lower()
    
#     try:
#         if file_name.endswith(".csv") or file_name.endswith(".txt"):
#             try:
#                 candidates_df = pd.read_csv(db_file, encoding="utf-8")
#             except UnicodeDecodeError:
#                 candidates_df = pd.read_csv(db_file, encoding="latin-1")

#             st.success("Candidate data uploaded successfully!")
#             st.dataframe(candidates_df)

#             # Add your shortlist logic here...
#             shortlisted_df = candidates_df.head(3)
#             st.subheader("✅ Shortlisted Candidates (Mock Output)")
#             st.dataframe(shortlisted_df)

#             if st.button("📤 Send Interview Invites"):
#                 st.success("Invites sent to shortlisted candidates!")

#         elif file_name.endswith(".pdf"):
#             reader = PyPDF2.PdfReader(db_file)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#             st.success("PDF Resume Text Extracted!")
#             st.text_area("📄 Resume Text", text[:1000])  # Preview first 1000 chars

#         else:
#             st.error("Unsupported file type.")

#     except Exception as e:
#         st.error(f"❌ Error while processing file: {str(e)}")



# import PyPDF2

st.subheader("👨‍💼 Upload Candidate Resume (.pdf)")
db_file = st.file_uploader("Upload candidate resume file", type=["pdf"])

if db_file:
    try:
        reader = PyPDF2.PdfReader(db_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text() or ""

        if resume_text.strip() == "":
            st.error("No text could be extracted from this PDF.")
        else:
            st.success("✅ Resume text extracted!")
            st.text_area("📄 Extracted Resume Text", resume_text[:2000], height=300)
    except Exception as e:
        st.error(f"❌ Error reading PDF: {str(e)}")





# Footer
st.markdown("---")
st.caption("Made with ❤️ for Hackathons | Team Recruiting_Rangers 🧙‍♂️")
