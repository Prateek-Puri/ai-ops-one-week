# AI Ops One-Week Portfolio
# AI Ops One-Week Portfolio

## Day 1 Summary
- Model reduces MAE vs naive baseline by **11.9%** on holdout.
- Top drivers: **promo**, **price**.
- Seasonality present - adjust safety stock accordingly.
- Segment variance differs - consider segment specific policies.
- Next 48 hours - add calendar features and run a small price promo test.

## Day 1 Artifacts
- Notebook: `ml-model/01_baseline.ipynb`
- Chart: `ml-model/figures/actual_vs_pred.png`
- Importances CSV: `ml-model/figures/feature_importances.csv`
- So what note: `ml-model/SO_WHAT.txt`

## Day 1 Artifact Links (make these clickable once your repo is public)
Replace `<USER>` with your GitHub username:
- Notebook: `https://github.com/<USER>/ai-ops-one-week/blob/main/ml-model/01_baseline.ipynb`
- Chart: `https://github.com/<USER>/ai-ops-one-week/blob/main/ml-model/figures/actual_vs_pred.png`
- Repo root: `https://github.com/<USER>/ai-ops-one-week`

**Day 1 WOW**
- Overbooking policy: converts predicted no show risk into extra bookings per block at a chosen service level. See overbooking_policy.csv and figures/day1_overbooking_policy.png.
- Smart micro windows: two non adjacent blocks to target with a small offer that fills valleys without creating peaks. See smart_windows.csv and figures/day1_smart_windows.png.
- Policy frontier: simple chart to pick discount and risk tolerance. See policy_frontier.csv and figures/day1_policy_frontier.png.


---

## Day 2 Summary
- Compared 4 week seasonal baseline vs model. MAE uplift: **24.7%**.
- Partial effects: price tends to reduce demand, promo adds lift.
- Top drivers: **price**, **promo**
- Artifacts:
  - ml-model/figures/day2_actual_model_baseline.png
  - ml-model/figures/day2_partial_price.png
  - ml-model/figures/day2_partial_promo.png
  - ml-model/figures/day2_feature_importances.csv

  ## Day 3 Summary
- Built a browser-only TF-IDF Q and A over Markdown SOPs and KPI glossary.
- Endpoints: `GET /` health, `POST /ask` returns top-k snippets with sources.
- No paid APIs. Runs entirely in Codespaces.

### Artifacts
- `rag-assistant/app.py`
- `docs/kpi_glossary_example.md`
- `docs/sop_example_inventory.md`
- (optional) `docs/screenshots/day3_health.png`, `docs/screenshots/day3_ask.png`


  ## Day 4 Summary
- Workforce linear program meets 7 day demand with minimum cost and a clear overtime tradeoff.
- Sensitivity: report cost at 0.9x, 1.0x, 1.1x, 1.2x demand.
- Artifacts:
  - optimizer/figures/day4_sensitivity.png
  - optimizer/SO_WHAT_DAY4.txt

## Day 5 Summary
- Two page executive memo that ties baselines, model uplift, optimization tradeoffs, and the RAG assistant into actions and risks.
- Artifacts:
  - docs/executive_memo.md
  - (optional) docs/executive_memo.pdf

## Day 6 Summary
- Learning notes and governance checklist that explain rigor, limits, and guardrails.
- Artifacts:
  - docs/day6_notes.md

## Day 7 Summary
- Slides outline and talk track to present the week.
- Repo polish: consistent artifact links, clear steps to reproduce.

### Artifacts
- docs/day7_slides_outline.md
- docs/day7_talk_track.md


## Structure

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
