# Executive Memo — AI-enabled Strategy and Operations (Template)

**Date:** 2025-10-04
**Author:** Your Name

## 1. Problem and Baseline
- Context: what process or KPI are we improving
- Baseline performance: simple seasonal or majority baseline
- Data scope and caveats

## 2. Predictive Model — What it does and why it matters
- Target: demand or churn
- Key features: recency, frequency, promo, price, seasonality
- Metrics: MAE or RMSE (demand), PR AUC or F1 (churn)
- Top 3 levers from feature importance or SHAP

## 3. Optimization — Tradeoffs and plan
- Decision variables and constraints
- Objective: cost vs service
- Sensitivity: ±10 percent on demand or labor cost, impact on cost and service

## 4. RAG Assistant — Knowledge access
- Sources: SOPs and KPI glossary in Markdown
- Example questions and answers
- Guardrails and citations

## 5. Risks, Controls, Next Steps
- Data quality checks, retraining cadence, access control
- Change management
- What to productionize next and expected impact
