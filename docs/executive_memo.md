# Executive Memo - AI enabled Strategy and Operations

**Date:** 2025-10-04  
**Author:** Prateek 

## 1) Problem and baseline
- Goal: improve forecast accuracy to reduce stockouts and working capital.
- Scope: weekly demand by product and region on sample transactional data.
- Baselines used:
  - Day 1: naive mean with simple calendar features.
  - Day 2: seasonal 4 week rolling mean per product and region.

## 2) Predictive model summary
- Day 1 uplift vs naive: **11.9% MAE** on holdout.
- Day 2 uplift vs seasonal 4 week: **24.7% MAE** on time ordered holdout.
- Top drivers so far: **promo**, **price**.
  - Partial effect: price shows a downward slope vs demand.
  - Partial effect: promo shows positive lift.
- Actions:
  - Keep seasonal baseline as a safety stock guardrail.
  - Use the model to prioritize promo and price cells for high value SKUs.

## 3) Optimization and tradeoffs
- Workforce linear program meets 7 day demand at minimum cost with overtime as a valve.
- Sensitivity: optimal cost increases as demand scale moves from 1.0x to 1.2x.
- Recommendations:
  - Set a daily overtime cap.
  - Cross train to reduce overtime spikes.
  - Next: add headcount ramp limits and a minimum days on shift rule.

## 4) RAG assistant for SOP and KPI questions
- Lightweight TF IDF retrieval over Markdown SOPs and the KPI glossary.
- Endpoints: GET / for health, POST /ask returns top snippets with sources.
- Use cases: define OTIF in a consistent way, provide a talk track for monthly ops review.

## 5) Risks and controls
- Data quality: check missingness, outliers, and leakage before training.
- Modeling: monthly retrain and weekly error review against a clear baseline.
- AI guardrails: insist on source citations, reject out of scope questions, keep human in the loop for SOP edits.

## 6) 30 60 90 plan
- 30 days: add holiday features and region segmentation, tighten MAPE reporting.
- 60 days: inventory linear program with service level target, BI handoff of KPIs.
- 90 days: packaging for cloud deploy, monitoring, governance signoff.

## Appendix - links
- Day 1 notebook: `ml-model/01_baseline.ipynb`
- Day 2 notebook: `ml-model/02_forecast_plus_drivers.ipynb`
- Day 4 sensitivity chart: `optimizer/figures/day4_sensitivity.png`
- RAG app: `rag-assistant/app.py`
