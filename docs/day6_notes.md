# Day 6 — Learning notes and governance

## What I validated this week
- Baselines matter: I reported uplift against naive (Day 1) and a seasonal 4 week baseline (Day 2). This increases trust in the improvement number.
- Drivers are controllable: promo and price repeatedly rank top. Partials show price tends to reduce demand and promo adds lift.
- Time awareness helps: a time ordered split was used on Day 2 so evaluation matches reality.

## What I will not claim yet
- Long horizon accuracy: current features are simple calendar and price/promo. No holiday features or domain events yet.
- Full generalization: results are from a sample retail like dataset. Will validate on a second dataset before claiming robustness.

## Responsible use and guardrails
- Retrieval: the Day 3 assistant returns snippets plus source file names. It rejects empty questions. No free text generation beyond the snippet.
- Data checks: confirm no target leakage, inspect missingness and outliers, log data ranges per training run.
- Model governance: keep the seasonal baseline as a safety stock guardrail, review error weekly, retrain monthly or when drift triggers.
- Decision cadence: weekly review that maps forecast error to OTIF and working capital; clear owners and next actions.

## Upgrade plan
- Features: add holiday calendar and simple event flags.
- Evaluation: blocked or sliding window time series CV.
- Inventory LP: add a service level constraint and translate into safety stock changes.
- RAG: include Markdown headings in chunk titles for clearer answers.

## Open risks
- Data drift by region: segment specific policies may be required.
- Promo cannibalization: include experiment design before policy changes.
- Operational adoption: change management and SOP updates needed for rollout.

## References to repo artifacts
- Day 1: ml-model/01_baseline.ipynb, figures and SO_WHAT.txt
- Day 2: ml-model/02_forecast_plus_drivers.ipynb, day2 figures
- Day 3: rag-assistant/app.py, docs markdown sources
- Day 4: optimizer/inventory_or_workforce.ipynb, day4_sensitivity.png
- Day 5: docs/executive_memo.md
