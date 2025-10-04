# AI Ops One-Week Portfolio

This repository contains three tangible deliverables you can finish in seven days:
1. **ML model** for demand or churn with clear business readout.
2. **RAG Ops Assistant** that answers SOP and KPI questions from local markdown sources with citations.
3. **Optimization model** for inventory or workforce planning with sensitivity.
4. **Executive memo** and short screen recordings tying everything together.

## Structure
```
ml-model/                   # Notebooks for baseline and drivers
rag-assistant/              # Simple FastAPI app + local vector store (Chroma)
optimizer/                  # Linear or integer programming notebook
docs/                       # Executive memo template, SOPs, KPI glossary
data/                       # Sample CSV and placeholders
```

## Quickstart
1. Create a Python 3.10+ virtual environment and install packages:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the **baseline ML notebook** in `ml-model/01_baseline.ipynb` and save metrics images to `ml-model/figures/`.

3. Launch the **RAG app** from `rag-assistant/`:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
   Then open http://127.0.0.1:8000 and use the `/ask` endpoint via Swagger UI to test.

4. Open the **optimizer notebook** in `optimizer/inventory_or_workforce.ipynb`, choose inventory or workforce mode, and run the sensitivity cell.

5. Export `docs/executive_memo_template.md` to PDF and update `README.md` with links to your artifacts and videos.
