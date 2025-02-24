# caption.py
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama

def generate_caption(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    llm = ChatOllama(model="llama3.1:8b", temperature=0)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
    chunks = text_splitter.create_documents([text])

    map_prompt_template = PromptTemplate(input_variables=['text'], template="Please generate a caption for the speech: `{text}`")
    final_combine_prompt_template = PromptTemplate(input_variables=['text'], template="Provide a caption for the speech in no more than 5 words: `{text}`")

    caption_chain = load_summarize_chain(
        llm=llm,
        chain_type='map_reduce',
        map_prompt=map_prompt_template,
        combine_prompt=final_combine_prompt_template
    )

    output = caption_chain.run(chunks)

    with open('caption_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output)
    return output
