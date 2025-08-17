
# BuggBit — AI-Powered Bug Reproduction & Triage

This is a scaffold to start building BuggBit: FastAPI backend (Python), MySQL, and a Next.js (TS) web UI.
- API: `/api`
- NLP/ML: `/nlp`
- Web UI: `/web`
- Infra/Docker: `/infra`

## Quick start (local)
1) Copy `.env.example` to `.env` and set secrets.
2) `docker compose -f infra/docker-compose.yml up -d`
3) `uvicorn api.main:app --reload` (from the repo root or `api/`)
4) Open the web app docs *(to be implemented)* at `web/`.
