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
