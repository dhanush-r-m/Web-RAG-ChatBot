## 🔎 Web RAG Chatbot

An end-to-end Retrieval-Augmented Generation (RAG) chatbot built with:

🌐 Firecrawl → Crawl and extract website content

🧠 ChromaDB → Vector database for storing embeddings

⚡ Ollama (local LLM) → Answer user queries with local/self-hosted models (e.g., Mistral, Llama 3)

💬 Chainlit → Chat UI for interacting with the bot

This project lets you crawl websites → embed content → ask questions → get grounded answers via a simple web interface.

---

## ✨ Features

🔍 Crawl any website with Firecrawl

📦 Store embeddings locally in ChromaDB

🖥️ Use Ollama for both embeddings (nomic-embed-text) and LLM inference (mistral, llama3, etc.)

💬 Chat with your documents in Chainlit UI

🔄 Reset & re-ingest data easily

---
## 📂 Project Structure

```
web-rag-chatbot/
├── crawler/
│   ├── firecrawl_crawl.py
│   ├── ingest.py
│   └── requirements.txt
├── rag_backend/
│   ├── app.py                 # chainlit entry / web UI integration
│   ├── rag.py                 # retrieval + LLM orchestration
│   ├── utils.py
│   ├── requirements.txt
│   └── .env.example
├── chroma/                    # optional: scripts to manage chroma
│   └── reset_chroma.py
├── docker-compose.yml         # optional: run chroma (if using server) / chainlit
├── README.md
└── LICENSE

```
---

## ⚡ Setup
1. Clone Repo
```
git clone https://github.com/dhanush-r-m/Web-RAG-ChatBot.git
cd web-rag-chatbot
```
2. Install Python Dependencies
```
pip install -r requirements.txt
```
3. Install & Run Ollama
```
Download Ollama (Mac, Linux, Windows WSL supported)
Pull required models:

ollama pull mistral
ollama pull nomic-embed-text
```

4. Crawl & Ingest Data
```
python crawler/ingest.py --url https://example.com
```

This extracts website content and stores embeddings in ChromaDB.

5. Run the Chatbot
```
chainlit run app.py

```
Open → http://localhost:8000

🔄 Reset Database

To clear embeddings and start fresh:
```
python chroma/reset_chroma.py
```
⚙️ Configuration

Set models in .env:
```
EMBED_MODEL=nomic-embed-text
LLM_MODEL=mistral
CHROMA_DIR=./chroma_store
```

