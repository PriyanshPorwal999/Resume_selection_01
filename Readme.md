# 🧠 Enhancing Job Screening with AI and Data Intelligence

This project was built as part of a hackathon challenge to automate and enhance the recruitment process using a multi-agent AI system. It aims to eliminate manual screening inefficiencies by using intelligent agents to read job descriptions, analyze resumes, match candidates, and schedule interviews—all while presenting useful data insights to HR teams.

---

## 🚀 Problem Statement

Recruitment is often slow, biased, and error-prone due to manual review of numerous job descriptions (JDs) and CVs. Our solution tackles this by automating the hiring pipeline through AI, improving speed, accuracy, and decision-making.

---

## 💡 Proposed Solution

- **JD Summarizer Agent**: Uses LLMs to extract key elements from job descriptions.
- **Resume Extractor Agent**: Parses candidate CVs to extract skills, education, experience, and certifications.
- **Matching Agent**: Calculates match score between JD and CV using keyword relevance and weighted scoring.
- **Shortlisting Module**: Automatically filters candidates with a match score above a predefined threshold.
- **Interview Scheduler Agent**: Sends automated, personalized interview invites via email.
- **Resume Analytics Dashboard**: Displays visual insights (charts, graphs) about candidates to assist HR in decision-making.
- **Memory System**: Uses SQLite to store summaries, scores, and resume data for long-term access.

---

## 🧰 Technology Stack

### 🔹 Frontend
- Streamlit  
- HTML/CSS (via Streamlit components)

### 🔹 Backend
- Python  
- SQLite  
- (Optional: Flask for API endpoints)

### 🔹 AI/ML
- Ollama (3.2:1b model)  
- Scikit-learn  
- Pandas, NumPy  
- Pickle

### 🔹 Data Visualization
- Matplotlib, Seaborn  
- (Optional: Plotly for interactivity)

### 🔹 Version Control
- Git & GitHub

### 🔹 Communication
- SMTP for sending emails  
- (Optional: Jinja2 for templated email content)

---

## 📁 Project Structure

