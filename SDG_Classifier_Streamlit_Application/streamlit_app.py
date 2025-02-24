import streamlit as st
import regex as re
import fitz  # PyMuPDF
from docx import Document
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import plotly.express as px
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')




st.set_page_config(
    page_title="SDG Classifier", layout="wide", initial_sidebar_state="auto", page_icon="🚦"
)


# Layout for logos
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image(r"D:\Sonali_AI_Projects\Woxsen_Projects\SDG\pdf_data\AIRC.jpeg", width=150)  # Replace with actual path or URL
with col3:
    st.image(r"D:\Sonali_AI_Projects\Woxsen_Projects\SDG\pdf_data\Wox.jpeg", width=500)  # Replace with actual path or URL


def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def extract_text_from_docx(docx_file):
    """Extract text from an uploaded DOCX file."""
    doc = Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def prep_text(text):
    """Preprocess text for classification."""
    clean_sents = []
    sent_tokens = sent_tokenize(str(text))
    for sent_token in sent_tokens:
        word_tokens = [str(word_token).strip().lower() for word_token in sent_token.split()]
        clean_sents.append(' '.join((word_tokens)))
    joined = ' '.join(clean_sents).strip(' ')
    joined = re.sub(r'`', "", joined)
    joined = re.sub(r'"', "", joined)
    return joined

checkpoint = "sadickam/sdg-classification-bert"

@st.cache_resource
def load_model():
    return AutoModelForSequenceClassification.from_pretrained(checkpoint)

@st.cache_data
def load_tokenizer():
    return AutoTokenizer.from_pretrained(checkpoint)

st.header("🚦 Sustainable Development Goals (SDG) Document Classifier")

st.markdown("##### Upload Documents (Up to 10 PDFs or DOCX Files)")
uploaded_files = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"], accept_multiple_files=True)
submitted = st.button("👉 Get SDG Predictions!")

if submitted and uploaded_files:
    results = []
    
    for uploaded_file in uploaded_files:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_extension == "docx":
            extracted_text = extract_text_from_docx(uploaded_file)
        else:
            st.error(f"Unsupported file format: {uploaded_file.name}. Please upload a PDF or DOCX file.")
            continue
        
        if not extracted_text.strip():
            st.warning(f"The document {uploaded_file.name} does not contain extractable text.", icon="⚠️")
            continue
        
        joined_clean_sents = prep_text(extracted_text)
        tokenizer_ = load_tokenizer()
        tokenized_text = tokenizer_(joined_clean_sents, return_tensors="pt", truncation=True, max_length=512)
        
        model = load_model()
        text_logits = model(**tokenized_text).logits
        predictions = torch.softmax(text_logits, dim=1).tolist()[0]
        predictions = [round(a, 3) for a in predictions]
        
        label_list = [
            'GOAL 1: No Poverty', 'GOAL 2: Zero Hunger', 'GOAL 3: Good Health and Well-being',
            'GOAL 4: Quality Education', 'GOAL 5: Gender Equality', 'GOAL 6: Clean Water and Sanitation',
            'GOAL 7: Affordable and Clean Energy', 'GOAL 8: Decent Work and Economic Growth',
            'GOAL 9: Industry, Innovation and Infrastructure', 'GOAL 10: Reduced Inequality',
            'GOAL 11: Sustainable Cities and Communities', 'GOAL 12: Responsible Consumption and Production',
            'GOAL 13: Climate Action', 'GOAL 14: Life Below Water', 'GOAL 15: Life on Land',
            'GOAL 16: Peace, Justice and Strong Institutions',
            'GOAL 17: Partnerships for the Goals'
        ]
        
        pred_dict = dict(zip(label_list, predictions))
        sorted_preds = sorted(pred_dict.items(), key=lambda x: x[1], reverse=True)
        
        results.append({
            "Filename": uploaded_file.name,
            "Predicted SDG": sorted_preds[0][0]
        })
        
        df2 = pd.DataFrame({'SDG': [x[0] for x in sorted_preds], 'Likelihood': [x[1] for x in sorted_preds]})
        
        st.markdown(f"##### Prediction Outcome for {uploaded_file.name}") 
        fig = px.bar(df2, x="Likelihood", y="SDG", orientation="h")
        fig.update_layout(template='seaborn', width=800, height=500)
        st.plotly_chart(fig)
        
        st.success(f"Predicted SDG for {uploaded_file.name}: {sorted_preds[0][0]} with {round(sorted_preds[0][1] * 100, 1)}% confidence.")
    
    if results:
        df_results = pd.DataFrame(results)
        df_results.to_excel("SDG_Predictions.xlsx", index=False)
        st.markdown("### Download Results")
        st.download_button(
            label="📥 Download SDG Predictions Excel File",
            data=df_results.to_csv(index=False).encode('utf-8'),
            file_name="SDG_Predictions.csv",
            mime="text/csv"
        )
