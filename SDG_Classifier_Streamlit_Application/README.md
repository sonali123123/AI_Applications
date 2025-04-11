## SDG Classifier Streamlit Application

This application is designed to classify documents (PDFs and DOCX files) into one of the United Nations Sustainable Development Goals (SDGs). The app processes the uploaded documents, extracts the text, preprocesses it, and then uses a language model to classify the content into the relevant SDG. It also generates a certificate with the SDG classification.

## Features

Document Upload: Users can upload multiple PDFs or DOCX files.

Text Extraction: The app extracts text from PDF and DOCX files.

SDG Classification: The app classifies the extracted text into one of the 17 SDGs based on predefined keywords.

Certificate Generation: A downloadable certificate is generated for the classified SDG.



## Requirements

Ensure that you have the following Python packages installed:

streamlit

streamlit-components

regex

PyMuPDF (for PDF text extraction)

python-docx (for DOCX text extraction)

pandas

nltk

base64

langchain

langchain-ollama

### You can install the necessary dependencies using:

pip install streamlit regex PyMuPDF python-docx pandas nltk base64 langchain langchain-ollama


### How to Run

Clone this repository to your local machine.

### Navigate to the project directory.

Run the following command to start the Streamlit app:

streamlit run app.py

This will launch a local server and you can access the app in your browser at http://localhost:8501.

### Application Workflow

Upload Documents: Users can upload PDFs or DOCX files by clicking the "Upload PDF or DOCX" button.

Text Extraction: The app extracts the text from the uploaded files using PyMuPDF for PDFs and python-docx for DOCX files.

Preprocessing: The extracted text is tokenized and cleaned for classification.

SDG Prediction: The app uses a pre-trained language model (ChatOllama) to predict the relevant SDG based on the extracted text. It checks for keyword matches related to SDGs and generates the most relevant classification.

Certificate Generation: Once the SDG is classified, a certificate HTML is generated, showcasing the classified SDG. You can view and download the certificate.

### SDG Goals List

The app uses predefined keywords for each SDG to match the text to one of the 17 SDGs as listed below:

GOAL 1: No Poverty

GOAL 2: Zero Hunger

GOAL 3: Good Health and Well-being

GOAL 4: Quality Education

GOAL 5: Gender Equality

GOAL 6: Clean Water and Sanitation

GOAL 7: Affordable and Clean Energy

GOAL 8: Decent Work and Economic Growth

GOAL 9: Industry, Innovation and Infrastructure

GOAL 10: Reduced Inequality

GOAL 11: Sustainable Cities and Communities

GOAL 12: Responsible Consumption and Production

GOAL 13: Climate Action

GOAL 14: Life Below Water

GOAL 15: Life on Land

GOAL 16: Peace, Justice and Strong Institutions

GOAL 17: Partnerships for the Goals

## Output

SDG Prediction: For each uploaded document, the app predicts which SDG it belongs to based on the text content.

Certificate: After classification, a certificate is displayed with the classified SDG and the option to download the certificate as HTML.

## Example Use Case

Upload a document that discusses issues related to hunger or food security.

The app processes the document and classifies it under GOAL 2: Zero Hunger.

A downloadable certificate is generated to confirm the classification.
