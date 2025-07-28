import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to calculate similarity
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(float(similarity[0][0]) * 100, 2)

# Streamlit App
st.title(" Resume Matcher ATS")

uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste the Job Description Here")

if uploaded_resume and job_description:
    resume_text = extract_text_from_pdf(uploaded_resume)
    match_score = calculate_similarity(resume_text, job_description)
    
    st.success(f"Your Resume Match Score: {match_score}%")
    
    if match_score >= 70:
        st.balloons()
        st.write(" Great match! You're likely a strong fit.")
    elif match_score >= 40:
        st.warning("Decent match. Consider tailoring your resume more.")
    else:
        st.error("Low match. Customize your resume better for this job.")
