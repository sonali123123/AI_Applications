import streamlit as st
import streamlit.components.v1 as components
import regex as re
import fitz  # PyMuPDF
from docx import Document
import pandas as pd
import nltk
import re
import base64
from nltk.tokenize import sent_tokenize
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

nltk.download('punkt')

st.set_page_config(
    page_title="SDG Classifier", layout="wide", initial_sidebar_state="auto", page_icon="🚦"
)



def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"


# Layout for logos
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image(r"D:\Sonali_AI_Projects\Woxsen_Projects\AI_Tools\SDG_Classifier_Streamlit_Application\\Img\AIRC.jpeg", width=150)  # Replace with actual path or URL
with col3:
    st.image(r"D:\Sonali_AI_Projects\Woxsen_Projects\AI_Tools\SDG_Classifier_Streamlit_Application\\Img\Wox.jpeg", width=500)  # Replace with actual path or URL


<<<<<<< HEAD
logo1_base64 = get_base64_image("Img\Wox.jpeg")

watermark_base64 = get_base64_image("Img\AIRC.jpeg")
=======
logo1_base64 = get_base64_image("pdf_data\Wox.jpeg")

watermark_base64 = get_base64_image("pdf_data\AIRC.jpeg")
>>>>>>> 3c446be130b95f44ac17d8f159c20784680fc473

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
        clean_sents.append(' '.join(word_tokens))
    joined = ' '.join(clean_sents).strip(' ')
    joined = re.sub(r'`', "", joined)
    joined = re.sub(r'"', "", joined)
    return joined

# Initialize the LLaMA model
model = ChatOllama(model="llama3.1:8b", temperature=0)

st.header("🚦 Sustainable Development Goals (SDG) Document Classifier")
st.markdown("##### Upload Documents (Up to 10 PDFs or DOCX Files)")
uploaded_files = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"], accept_multiple_files=True)
submitted = st.button("👉 Get SDG Predictions!")

results = []
if submitted and uploaded_files:
    # Define SDG keywords (same as before)
    sdg_keywords = {
        'GOAL 1: No Poverty': ['poverty', 'poor', 'income', 'social protection', 'economic resources'],
        'GOAL 2: Zero Hunger': ['hunger', 'food security', 'nutrition', 'agriculture'],
        'GOAL 3: Good Health and Well-being': ['health', 'well-being', 'disease', 'vaccination'],
        'GOAL 4: Quality Education': ['education', 'school', 'literacy', 'learning'],
        'GOAL 5: Gender Equality': ['gender', 'equality', 'women', 'empowerment'],
        'GOAL 6: Clean Water and Sanitation': ['water', 'sanitation', 'hygiene'],
        'GOAL 7: Affordable and Clean Energy': ['energy', 'renewable', 'electricity'],
        'GOAL 8: Decent Work and Economic Growth': ['employment', 'economic growth', 'job'],
        'GOAL 9: Industry, Innovation and Infrastructure': ['industry', 'innovation', 'technology'],
        'GOAL 10: Reduced Inequality': ['inequality', 'social inequality', 'discrimination'],
        'GOAL 11: Sustainable Cities and Communities': ['urban', 'sustainable', 'housing'],
        'GOAL 12: Responsible Consumption and Production': ['consumption', 'production', 'waste'],
        'GOAL 13: Climate Action': ['climate', 'global warming', 'carbon'],
        'GOAL 14: Life Below Water': ['ocean', 'marine', 'sea'],
        'GOAL 15: Life on Land': ['forest', 'biodiversity', 'wildlife'],
        'GOAL 16: Peace, Justice and Strong Institutions': ['peace', 'justice', 'governance'],
        'GOAL 17: Partnerships for the Goals': ['partnerships', 'collaboration']
    }
    
    # Create a prompt template with SDG keywords
    prompt_template = ChatPromptTemplate.from_template("""
    Classify the following text into one of the Sustainable Development Goals (SDGs) based on the keywords provided:
    
    Text: {context}
    
    SDG Keywords:
    {sdg_keywords}
    
    Please provide the most relevant SDG goal for the given text. 
    Also mention the reason behind choosing that SDG category in 50 words.                                                
    """)
    
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
        prompt = prompt_template.format(context=joined_clean_sents, sdg_keywords=sdg_keywords)
        response = model.predict(prompt)
        predicted_sdg = response.strip()  # Assuming the response is a string
        
        results.append({
            "Filename": uploaded_file.name,
            "Predicted SDG": predicted_sdg
        })
        
        st.markdown(f"##### Prediction Outcome for {uploaded_file.name}") 
        st.success(f"Predicted SDG for {uploaded_file.name}: {predicted_sdg}")
    
    if results:
        df_results = pd.DataFrame(results)
<<<<<<< HEAD
=======
        # st.markdown("### Download Results")
        # st.download_button(
        #     label="📥 Download SDG Predictions CSV File",
        #     data=df_results.to_csv(index=False).encode('utf-8'),
        #     file_name="SDG_Predictions.csv",
        #     mime="text/csv"
        # )
        
        # For demonstration, we'll generate a certificate for the first processed file.
        # You can extend this logic to allow users to select which certificate they want.
>>>>>>> 3c446be130b95f44ac17d8f159c20784680fc473
        first_result = results[0]
        predicted_sdg = first_result["Predicted SDG"].replace('*','')

        def extract_goal(predicted_sdg):
<<<<<<< HEAD
    
=======
    # Search for the pattern "GOAL" followed by a number, a colon, and the rest of the string.
>>>>>>> 3c446be130b95f44ac17d8f159c20784680fc473
             
                predicted_sdg = predicted_sdg.replace('*', '')
                
                # Find the index of the first occurrence of "GOAL".
                idx = predicted_sdg.find("GOAL")
                
                # If "GOAL" is found, return the substring from that point to the end.
                if idx != -1:
                    return predicted_sdg[idx:]
                else:
                    return "No SDG found in the provided string."
        print(predicted_sdg)

        # Extract the goal from the cleaned string
        extracted_goal = extract_goal(predicted_sdg)
        print("Extracted SDG:", extracted_goal)
        
        # Certificate HTML template with dynamic SDG category
        certificate_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Certificate of SDG Classification Excellence</title>
          <style>
            body {{
              font-family: 'Times New Roman', serif;
              background: #f7f7f7;
              padding: 20px;
            }}
            .certificate {{
              width: 700px;
              height: 500px;
              margin: 0 auto;
              padding: 40px;
              background: #fff;
              border: 10px solid #d4af37;
              position: relative;
              overflow: hidden;
            }}
            /* Watermark Logo */
            .watermark {{
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
              opacity: 0.1;
              width: 500px;
              height: auto;
              z-index: 1;
            }}
            .logos {{
              display: flex;
              justify-content: space-between;
              align-items: center;
              position: relative;
              z-index: 2;
            }}
            .logos img {{
              width: 160px;
              height: auto;
            }}
            .content {{
              text-align: center;
              margin-top: 60px;
              position: relative;
              z-index: 2;
            }}
            /* Title font: Congenial Bold */
            .content h1,
            .content p {{
              font-family: "Times New Roman", cursive;
              font-weight: bold;
            }}
            .content h1 {{
              font-size: 36px;
              margin-bottom: 20px;
            }}
            /* Paragraph font: Gabriola (italic) with justified alignment */
    .content p {{
                font-family: "Georgia Pro";
                
                font-size: 17px;
                line-height: 1.5;
                margin: 0 20px;
                text-align: justify;
         }}

    /* Certification text in place of signature */
    .certified {{
            position: absolute;
            bottom: 20px;
            right: 40px;
            font-family: "Gabriola", cursive;
            font-style: italic;
            font-size: 40px;
            z-index: 2;
            color: #000;
    }}
          </style>
        </head>
        <body>
          <div class="certificate">
            <!-- Watermark Logo -->
            <img src="{watermark_base64}" alt="Watermark Logo" class="watermark">
            <!-- Top logos -->
            <div class="logos">
              <img src="{logo1_base64}" alt="Logo 1">
              
            </div>
            <!-- Certificate content -->
            <div class="content">
              <h1>Certificate of SDG Classification Excellence</h1>
              <p>
                This document is classified under <strong>{extracted_goal}</strong> 
              </p>
            </div>
            <!-- Certified by AIRC block in place of signature -->
            <div class="certified">
            Certified by AIRC - Woxsen University
            </div>
          </div>
        </body>
        </html>
        """
        st.markdown("### Your Certificate")
        # Embed the certificate HTML in your Streamlit app
        components.html(certificate_html, height=650, scrolling=True)
        
        # Optionally, you can add a download button for the certificate (e.g., generate PDF from HTML via another library)
        st.download_button(
            label="📥 Download Certificate HTML",
            data=certificate_html,
            file_name="SDG_Certificate.html",
            mime="text/html"
        )
