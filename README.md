# AI Ops One-Week Portfolio
# AI Ops One-Week Portfolio

**Day 1 **
- Overbooking policy: converts predicted no show risk into extra bookings per block at a chosen service level. See overbooking_policy.csv and figures/day1_overbooking_policy.png.
- Smart micro windows: two non adjacent blocks to target with a small offer that fills valleys without creating peaks. See smart_windows.csv and figures/day1_smart_windows.png.
- Policy frontier: simple chart to pick discount and risk tolerance. See policy_frontier.csv and figures/day1_policy_frontier.png.


---

  ## Day 2  — From rules to an optimal plan
- Reliability: rolling, time-ordered backtest vs seasonal baseline.  
- Driver Cards: effect sizes and local elasticity with partial plots.  
- Segment Policy Cards: recommended actions by clinic or performance.  
- Optimal weekly plan: portfolio of discount windows and overbooking actions under a budget and risk cap.  
- Frontiers and pricing: profit vs budget curve and expected cost of a service guarantee.

Artifacts
- ml-model/driver_cards.csv
- ml-model/segment_policy_cards.csv
- ml-model/figures/day2_backtest.png
- ml-model/figures/day2_partial_*.png
- ml-model/figures/day2_allocation_frontier.png
- ml-model/figures/day2_guarantee_pricing.png
- ml-model/figures/day2_decision_board.png
- optimizer/campaign_plan.csv
- optimizer/allocation_frontier.csv
- optimizer/guarantee_pricing.csv


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

## Day 2 - Decisions and Allocation

- Reliability: rolling, time-ordered backtest vs a seasonal baseline.  
- Driver cards: effect sizes and local elasticity with partial plots.  
- Segment policy cards: recommended actions per segment.  
- Optimal plan: selected actions under a budget and a service risk cap.  
- Frontiers and pricing: profit vs budget curve and expected cost of a no-wait guarantee.  

**Backtest summary**  
- Folds: 100  
- Percent folds beating baseline: 70.0%  
- Average uplift vs seasonal baseline: 1.8%  
- Min uplift: -78.7%, Max uplift: 18.6%  

**Artifacts**  
- `ml-model/figures/day2_backtest.png`  
- `ml-model/driver_cards.csv`  
- `ml-model/segment_policy_cards.csv`  
- `ml-model/figures/day2_allocation_frontier.png`  
- `ml-model/figures/day2_guarantee_pricing.png`  
- `ml-model/figures/day2_decision_board.png`  
- `optimizer/campaign_plan.csv`, `optimizer/allocation_frontier.csv`, `optimizer/guarantee_pricing.csv`
