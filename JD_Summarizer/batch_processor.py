import csv
from job_description import JobDescription

def process_csv_file(csv_file_path, ollama_client=None):
    results = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            job_title = (row.get('Job Title') or row.get('job_title') or 
                         row.get('Title') or row.get('title') or '').strip()
            job_description = (row.get('Job Description') or row.get('job_description') or 
                               row.get('Description') or row.get('description') or '').strip()
            if job_title and job_description:
                jd = JobDescription(job_title, job_description, ollama_client)
                results.append(jd.to_dict())
    return results