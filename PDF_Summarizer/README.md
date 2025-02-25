## PDF Summarizer

A simple and efficient tool to summarize PDF documents using Streamlit, LangChain, and OpenAI. Upload one or multiple PDFs, and get concise summaries (4-5 sentences) in seconds.

## Overview

This application processes PDF files by extracting text, splitting it into chunks, embedding it with OpenAI, and storing it in a FAISS vector database. It then generates summaries using a question-answering chain, all wrapped in a sleek Streamlit interface.

## Features

Upload and summarize multiple PDFs at once.
Summaries generated in 4-5 sentences, prefixed with the file name.
Custom-styled Streamlit UI with a sidebar for file uploads.
Powered by OpenAI embeddings and LangChain for robust text processing.

## Tech Stack

Python
Streamlit ( Frontend )
LangChain ( Text Processing & Summarization )
OpenAI ( Embeddings & Language Model )
FAISS ( Vector Storage )
PyPDF2 ( PDF Text Extraction )


## Setup

1. Clone the Repo:

https://github.com/sonali123123/AI_Applications.git
cd PDF_Summarizer

2. Install Dependies

pip install -r requirements.txt

3. Set Up API Key

Create a constants.py file in the root directory
ADD:

openai_api_key = "your-openai-api-key"


## How to Run

1. Start the app

streamlit run frontened.py


## Ue the App:

Navigate to http://localhost:8501 in your browser.
Upload PDFs via the sidebar.
Click "Upload" to see summaries displayed below.