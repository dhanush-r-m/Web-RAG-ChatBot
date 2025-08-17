# rag_backend/app.py (Chainlit + Ollama)
import chainlit as cl
from rag_backend.rag import build_qa_chain, get_retriever

QA_CHAIN = build_qa_chain(model_name="llama3.1:8b") 

PROMPT_TEMPLATE = """You are a helpful assistant.
Use the CONTEXT below to answer. If unknown, say "I don't know".
CONTEXT:
{context}

QUESTION:
{question}
"""

@cl.on_message
async def main(message: cl.Message):
    query = message.content
    retriever = get_retriever()
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join(d.page_content[:1000] for d in docs[:3])
    prompt = PROMPT_TEMPLATE.format(context=context, question=query)
    resp = QA_CHAIN.run(query)

    sources = list({d.metadata.get("source", "") for d in docs if d.metadata.get("source")})
    content = resp + "\n\nSOURCES:\n" + "\n".join(sources)
    await cl.Message(content=content).send()
