from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import re, glob
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = Path(__file__).resolve().parents[1] / "docs"

app = FastAPI(
    title="RAG Ops Assistant (TF-IDF)",
    version="0.3.0",
    description="Browser-only Q&A over Markdown SOPs and KPI glossary. Returns snippets with sources."
)

class Ask(BaseModel):
    question: str
    k: int = 3  # how many snippets to return

def load_markdown_docs() -> List[Tuple[str, str]]:
    items = []
    for fp in glob.glob(str(DATA_DIR / "*.md")):
        p = Path(fp)
        try:
            txt = p.read_text(encoding="utf-8")
            items.append((p.name, txt))
        except Exception as e:
            print(f"Skip {p.name}: {e}")
    if not items:
        raise RuntimeError(f"No .md files found in {DATA_DIR}")
    return items

def chunk_text(name: str, text: str, size: int = 900) -> Tuple[List[str], List[str]]:
    # simple paragraph chunker with packing
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, sources = [], []
    buf = ""
    for para in paras:
        if len(buf) + len(para) < size:
            buf = (buf + "\n\n" + para).strip()
        else:
            if buf:
                chunks.append(buf); sources.append(name)
            buf = para
    if buf:
        chunks.append(buf); sources.append(name)
    return chunks, sources

# Build index at startup
RAW = load_markdown_docs()
CHUNKS, SOURCES = [], []
for name, txt in RAW:
    c, s = chunk_text(name, txt, size=900)
    CHUNKS.extend(c); SOURCES.extend(s)

VEC = TfidfVectorizer(lowercase=True, stop_words="english")
MATRIX = VEC.fit_transform(CHUNKS)

@app.get("/")
def root():
    return {
        "ok": True,
        "docs_indexed": [n for n, _ in RAW],
        "num_chunks": len(CHUNKS)
    }

@app.post("/ask")
def ask(q: Ask):
    qtext = q.question.strip()
    if not qtext:
        raise HTTPException(status_code=400, detail="Empty question")
    if not (1 <= q.k <= 10):
        raise HTTPException(status_code=400, detail="k must be 1..10")

    qv = VEC.transform([qtext])
    sims = cosine_similarity(qv, MATRIX)[0]
    idx = sims.argsort()[::-1][:q.k]

    answers = []
    for i in idx:
        snippet = CHUNKS[i]
        source = SOURCES[i]
        score = float(sims[i])
        answers.append({
            "score": round(score, 4),
            "source": source,
            "snippet": snippet[:600]
        })

    return {"question": qtext, "answers": answers}
