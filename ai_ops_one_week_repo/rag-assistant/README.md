# RAG Ops Assistant

This is a minimal FastAPI app that demonstrates the skeleton of a Retrieval-Augmented Generation workflow.

- It loads Markdown documents from `../docs`
- A proper version would:
  - Create embeddings for each chunk using a small open model
  - Store vectors in Chroma and perform similarity search
  - Feed retrieved context into a local LLM or an API
- This stub performs naive keyword retrieval so you can wire the UI and record a short demo today.

## Run
```bash
uvicorn app:app --reload --port 8000
```
Open http://127.0.0.1:8000/docs for Swagger UI.
