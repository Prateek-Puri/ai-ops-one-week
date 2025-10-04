
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import markdown
import glob
import chromadb

# This stub uses Chroma as an in-process vector store.
# For embeddings and text encoding, you can integrate sentence-transformers or an API later.
# Here we store raw text and do naive retrieval by substring as a placeholder, then return the most relevant chunks.

DATA_DIR = Path(__file__).resolve().parents[1] / "docs"

app = FastAPI(title="RAG Ops Assistant", version="0.1.0")

class Ask(BaseModel):
    question: str

def load_docs():
    docs = []
    for fp in glob.glob(str(DATA_DIR / "*.md")):
        p = Path(fp)
        txt = p.read_text(encoding="utf-8")
        docs.append((p.name, txt))
    return docs

DOCS = load_docs()

@app.get("/")
def root():
    return {"ok": True, "docs": [d[0] for d in DOCS]}

@app.post("/ask")
def ask(payload: Ask):
    q = payload.question.lower().strip()
    if not q:
        raise HTTPException(status_code=400, detail="Empty question")
    # Naive retrieval by keyword match count (placeholder for real embeddings search)
    scored = []
    for name, txt in DOCS:
        score = sum(q.count(tok) for tok in set(q.split())) + (1 if any(tok in txt.lower() for tok in q.split()) else 0)
        scored.append((score, name, txt))
    scored.sort(reverse=True, key=lambda x: x[0])
    top = scored[:2]
    if not top or top[0][0] == 0:
        return {"answer": "No direct match found. Try rephrasing the question.", "sources": []}
    # Compose a simple answer by extracting first paragraph from best doc
    name, txt = top[0][1], top[0][2]
    first_para = txt.strip().split("\n\n")[0]
    html = markdown.markdown(first_para)
    return {"answer_html": html, "sources": [t[1] for t in top]}
