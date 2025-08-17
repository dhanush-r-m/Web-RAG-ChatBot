import os
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

CHROMA_PERSIST_DIR = os.getenv("CHROMA_DIR", "../chroma_store")

def get_retriever(k=4, search_type="mmr"):

    embeddings = OllamaEmbeddings(model="nomic-embed-text")  
    db = Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=embeddings)
    retriever = db.as_retriever(search_type=search_type, search_kwargs={"k": k})
    return retriever

def build_qa_chain(model_name="llama3.1:8b", temperature=0.2):
    llm = ChatOllama(model=model_name, temperature=temperature)
    retriever = get_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa

def answer_query(query: str, qa_chain=None):
    qa = qa_chain or build_qa_chain()
    result = qa.run(query)
    return result
