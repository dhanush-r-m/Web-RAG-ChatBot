import os
import json
from typing import List
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

CHROMA_PERSIST_DIR = os.getenv("CHROMA_DIR", "./chroma_store")

def docs_to_langchain(firecrawl_docs: List[dict]):
    lc_docs = []
    for d in firecrawl_docs:
        text = d.get("text") or d.get("content") or ""
        meta = {"source": d.get("url"), "title": d.get("title", "")}
        if text.strip():
            lc_docs.append(Document(page_content=text, metadata=meta))
    return lc_docs

def ingest(docs: List[dict], persist=True):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")  
    lc_docs = docs_to_langchain(docs)
    db = Chroma.from_documents(lc_docs, embeddings, persist_directory=CHROMA_PERSIST_DIR)
    if persist:
        db.persist()
    return db
