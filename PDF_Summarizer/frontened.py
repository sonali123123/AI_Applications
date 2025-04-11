import streamlit as st
from backened import process_pdf_text  # Assuming backend.py contains the summarization logic

def main():
    st.set_page_config(page_title="PDF Summarizer", layout="wide")
    st.title("📄 PDF Summarizer with Ollama")
    
    st.markdown("Upload PDF files and get a concise summary powered by Llama3.1:8b.")
    
    uploaded_files = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        with st.spinner("Processing PDFs..."):
            process_pdf_text(uploaded_files)
    
if __name__ == "__main__":
    main()
