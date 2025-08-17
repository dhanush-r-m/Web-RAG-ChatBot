import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Load env vars at import
load_dotenv()

def get_env_var(name: str, default=None, required=False):
    """Fetch env var with optional default and required flag."""
    value = os.getenv(name, default)
    if required and value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def chunk_text(text: str, chunk_size=1000, overlap=200):
    """Split large text into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)

def normalize_docs(firecrawl_docs):
    """Convert Firecrawl JSON docs into LangChain Documents with chunks."""
    lc_docs = []
    for d in firecrawl_docs:
        text = d.get("text") or d.get("content") or ""
        meta = {"source": d.get("url"), "title": d.get("title", "")}
        chunks = chunk_text(text)
        for chunk in chunks:
            lc_docs.append(Document(page_content=chunk, metadata=meta))
    return lc_docs
