import streamlit as st
import nltk
from utils import extract_resume_text, clean_text, extract_skills, get_match_score, missing_skills

nltk.download('punkt')

st.title("📄 Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Enter Job Description")

if uploaded_file and job_description:

    # Process resume
    resume_text = extract_resume_text(uploaded_file)

    cleaned_resume = clean_text(resume_text)
    cleaned_job = clean_text(job_description)

    # Analysis
    skills = extract_skills(cleaned_resume)
    score = get_match_score(cleaned_resume, cleaned_job)
    missing = missing_skills(skills)

    # Output
    st.subheader("🔍 Analysis Result")
    st.write("**Skills Found:**", skills)
    st.write("**Match Score:**", str(score) + "%")

    if score < 50:
        st.warning("⚠️ Improve your resume")
    else:
        st.success("✅ Good match!")

    st.subheader("📉 Missing Skills")
    st.write(missing)