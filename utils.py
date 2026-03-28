import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text
from skills import skills_db

# Extract text from PDF
def extract_resume_text(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())
    return extract_text("temp.pdf")

# Clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    return text

# Extract skills
def extract_skills(text):
    return [skill for skill in skills_db if skill in text]

# Match score
def get_match_score(resume, job_desc):
    cv = CountVectorizer()
    matrix = cv.fit_transform([resume, job_desc])
    similarity = cosine_similarity(matrix)[0][1]
    return round(similarity * 100, 2)

# Missing skills
def missing_skills(found_skills):
    return [skill for skill in skills_db if skill not in found_skills]