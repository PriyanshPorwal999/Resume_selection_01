import re
from ollama_client import OllamaClient

class JobDescription:
    def __init__(self, title, description, ollama_client=None):
        self.title = title
        self.description = description
        self.ollama_client = ollama_client
        self.processed_text = self.preprocess_text(description)
        self.patterns = {
            'years_of_experience': r'(\d+\+?\s*(?:-|to)?\s*\d*\+?\s*years?(?:\s*of)?(?:\s*experience)?)',
            'education': r'((?:Bachelor\'?s?|Master\'?s?|MBA|PhD|Doctorate|BS|MS|BA|MA|MD|JD|B\.S\.|M\.S\.|B\.A\.|M\.A\.)(?:\s+degree)?(?:\s+in\s+[A-Za-z\s,]+)?)',
            'certifications': r'((?:certification|certificate|certified|CPA|PMP|CISSP|AWS|Azure|CCNA|MCSE|CISA|CFA|SHRM|PHR|SPHR)(?:\s*in\s*[A-Za-z\s,]+)?)',
        }

    def preprocess_text(self, text):
        cleaned_text = re.sub(r'\s+', ' ', text).strip()
        cleaned_text = re.sub(r'[^\w\s.,-:()/]', '', cleaned_text)
        return cleaned_text

    def extract_years_of_experience(self):
        matches = re.findall(self.patterns['years_of_experience'], self.processed_text, re.IGNORECASE)
        return list(set(matches)) if matches else []

    def extract_education(self):
        matches = re.findall(self.patterns['education'], self.processed_text, re.IGNORECASE)
        filtered_matches = [m for m in matches if len(m.split()) >= 2 or any(degree in m.upper() for degree in ["BS", "MS", "BA", "MA", "MBA", "PHD", "MD", "JD"])]
        return list(set(filtered_matches)) if filtered_matches else []

    def extract_certifications(self):
        matches = re.findall(self.patterns['certifications'], self.processed_text, re.IGNORECASE)
        return list(set(matches)) if matches else []

    def extract_skills(self):
        if self.ollama_client:
            prompt = f"""
            Extract the technical and soft skills required in this job description. 
            Return only a comma-separated list of skills, nothing else.

            Job Description:
            {self.processed_text}

            Skills:
            """
            response = self.ollama_client.generate(prompt)
            if response:
                skills = [skill.strip() for skill in response.split(',') if skill.strip()]
                return skills
        return self.extract_skills_fallback()

    def extract_skills_fallback(self):
        tech_skills = r'(Python|Java|JavaScript|C\+\+|C#|Ruby|PHP|SQL|HTML|CSS|React|Angular|Vue|Node\.js|Django|Flask|Spring|AWS|Azure|GCP|Docker|Kubernetes|Git|REST|API|JSON|XML|MongoDB|PostgreSQL|MySQL|Oracle|NoSQL|Linux|Windows|MacOS|Agile|Scrum|DevOps|CI/CD|TDD)'
        soft_skills = r'(communication|teamwork|leadership|problem.solving|analytical|critical.thinking|time.management|adaptability|creativity|collaboration|attention.to.detail|organization Facetune|organization|project.management)'
        tech_matches = re.findall(tech_skills, self.processed_text, re.IGNORECASE)
        soft_matches = re.findall(soft_skills, self.processed_text, re.IGNORECASE)
        return list(set(tech_matches + soft_matches))

    def extract_responsibilities(self):
        if self.ollama_client:
            prompt = f"""
            Extract the main responsibilities from this job description.
            Return a numbered list of 3-5 key responsibilities, one per line. Be concise.

            Job Description:
            {self.processed_text}

            Responsibilities:
            """
            response = self.ollama_client.generate(prompt)
            if response:
                responsibilities = [re.sub(r'^\d+\.\s*', '', line).strip() for line in response.split('\n') if line.strip()]
                return responsibilities
        return self.extract_responsibilities_fallback()

    def extract_responsibilities_fallback(self):
        resp_section = re.search(r'(?:Responsibilities|Duties|Key responsibilities|Role|What you\'ll do)(?:\s*:\s*|\s*\n)(.*?)(?:\n\s*(?:Qualifications|Requirements|Skills|About you|What you need|Education)|$)', self.processed_text, re.IGNORECASE | re.DOTALL)
        if resp_section:
            section_text = resp_section.group(1)
            items = re.split(r'[•\-\*]|\n+', section_text)
            responsibilities = [item.strip() for item in items if item.strip() and len(item.strip()) > 10]
            return responsibilities[:5]
        sentences = re.split(r'[.\n]', self.processed_text)
        action_verbs = ['develop', 'manage', 'create', 'design', 'implement', 'build', 'analyze', 'maintain', 'optimize', 'coordinate', 'lead', 'conduct']
        resp_candidates = [s.strip() for s in sentences if s.strip() and any(verb in s.lower() for verb in action_verbs)]
        return resp_candidates[:5] if resp_candidates else ["Unable to extract responsibilities"]

    def generate_summary(self):
        if self.ollama_client:
            prompt = f"""
            Summarize this job description in 1-2 sentences. Be concise and focus on the key requirements.

            Job Title: {self.title}
            Job Description:
            {self.processed_text}

            Summary:
            """
            response = self.ollama_client.generate(prompt)
            if response:
                return response
        resp = self.extract_responsibilities_fallback()
        return f"A {self.title} position with responsibilities related to {resp[0] if resp else 'the field'}."

    def to_dict(self):
        return {
            "job_title": self.title,
            "summary": self.generate_summary(),
            "years_of_experience": self.extract_years_of_experience(),
            "education": self.extract_education(),
            "certifications": self.extract_certifications(),
            "skills": self.extract_skills(),
            "core_responsibilities": self.extract_responsibilities()
        }