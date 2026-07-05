import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_resume(resume_text):
    prompt = f"""
You are an expert technical recruiter and resume reviewer.
Analyze the following resume and provide:
1. Overall strengths (3-4 points)
2. Weaknesses or gaps (3-4 points)
3. ATS (Applicant Tracking System) compatibility issues, if any
4. Specific suggestions to improve it for SDE/Full Stack roles

Resume text:
{resume_text}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("sample_resume.pdf")
    analysis = analyze_resume(resume_text)
    print(analysis)