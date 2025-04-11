import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import ollama

def get_ollama_response(pdf_content, prompt):
    response = ollama.generate(
        model="llama3.1:8b",
        prompt=f"Extract relevant information from the following resume:\n{pdf_content}\n\n{prompt}"
    )
    return response["response"]

def input_pdf_setup(uploaded_files):
    pdf_texts = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            pdf_texts.append(base64.b64encode(img_byte_arr).decode())
    return pdf_texts

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Predefined Job Description
job_description = """
Seeking a passionate AI Engineer with at least 1 year of experience to join our growing team. The ideal candidate should have hands-on experience
in Generative AI, fine-tuning Large Language Models (LLMs), and building AI-driven applications. You will be responsible for developing, optimizing, 
and deploying AI-powered solutions using the latest advancements in Agentic AI, OCR applications, and Computer Vision.

Required Skills & Qualifications
- 1+ year of experience in AI/ML development.
- Strong understanding of Generative AI techniques and tools.
- Experience in fine-tuning LLMs (e.g., OpenAI, Llama, Mistral, Falcon).
- Knowledge of Vector Databases (e.g., Pinecone, FAISS, Weaviate).
- Familiarity with OCR frameworks (e.g., Tesseract, EasyOCR, Google Vision API).
- Proficiency in Python, TensorFlow/PyTorch, and NLP frameworks.
- Experience in building and consuming RESTful APIs.
- Hands-on experience with Docker and Git for development and deployment.
- Understanding of Relational (PostgreSQL, MySQL) and NoSQL (MongoDB, Redis) Databases.
- Experience in Computer Vision and image processing techniques.

Preferred Skills (Nice to Have)
- Experience with LangChain, LlamaIndex, or RAG-based architectures.
- Familiarity with Kubernetes for AI model deployment.
- Experience in multi-modal AI applications.
"""

st.subheader("Predefined Job Description")
st.text(job_description)

uploaded_files = st.file_uploader("Upload up to 5 resumes (PDF)...", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write("PDFs Uploaded Successfully")

submit = st.button("Check Percentage Match")

input_prompt = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of job matching.
Evaluate the uploaded resume against the predefined job description and return the percentage match.
Provide a brief summary mentioning missing keywords and final thoughts.
Output format:
1. Percentage Match: XX%
2. Missing Keywords: [...]
3. Final Thoughts: [...]
"""

if submit:
    if uploaded_files:
        pdf_contents = input_pdf_setup(uploaded_files)
        for i, pdf_content in enumerate(pdf_contents):
            response = get_ollama_response(pdf_content, input_prompt)
            st.subheader(f"Matching Percentage for Resume {i+1}:")
            st.write(response)
    else:
        st.write("Please upload at least one resume.")
