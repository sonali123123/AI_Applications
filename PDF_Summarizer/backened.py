from InstructorEmbedding import INSTRUCTOR
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS 
import streamlit as st
from PyPDF2 import PdfReader
from langchain.chains.summarize import load_summarize_chain
from langchain_ollama import ChatOllama

# Initialize Ollama model
llm = ChatOllama(model="llama3.1:8b", temperature=0)


#This Function is responsible for summarizing the PDF fules
def multi_pdf_summariser(vectorstore):

    query = "Summarize the content of the uploaded PDF in 4-5 sentences. Start answer with File Name"

    if query:
        docs = vectorstore.similarity_search(query)
    
    summary_chain = load_summarize_chain(
        llm=llm,
        chain_type='map_reduce'
    )
    
    summary = summary_chain.run(docs)
    st.write(summary)

#This Function is for embedding the text chunks & storing them FAISS vector DB
def vector_store(text_chunks):
    #Embedding the Texts
    embeddings = INSTRUCTOR('hkunlp/instructor-xl',device="cuda")
    #FAISS - Create Vector Store
    vectorstore = FAISS.from_texts(text_chunks, embeddings)

    multi_pdf_summariser(vectorstore)

#This Function is for breaking texts into group of chunks
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    text_chunks = text_splitter.split_text(text = raw_text)
    vector_store(text_chunks)

#This function is used for extracting text from individual PDFs
#Once text is extracted from a single PDF, get_text_chunks will be called
def process_pdf_text(pdf):
    if pdf is not None:
        raw_text = ""
        count = 0
        for files in pdf:
            pdf_reader =PdfReader(files)
            for page in pdf_reader.pages:
                raw_text += page.extract_text() 
            get_text_chunks(raw_text)
        
            