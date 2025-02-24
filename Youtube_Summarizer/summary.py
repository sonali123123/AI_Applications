# summary.py
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama

def summarize_text_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    llm = ChatOllama(model="llama3.1:8b", temperature=0)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
    chunks = text_splitter.create_documents([text])

    map_prompt_template = PromptTemplate(input_variables=['text'], template="Please summarize the below speech: `{text}`")
    final_combine_prompt_template = PromptTemplate(input_variables=['text'], template="Provide a final summary of the entire speech: `{text}`")

    summary_chain = load_summarize_chain(
        llm=llm,
        chain_type='map_reduce',
        map_prompt=map_prompt_template,
        combine_prompt=final_combine_prompt_template
    )

    output = summary_chain.run(chunks)

    with open('summary_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output)
    return output
