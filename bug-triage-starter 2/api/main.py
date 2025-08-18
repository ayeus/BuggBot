from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import ingest, analyze, integrate, auth

app = FastAPI(title="Bug Reproduction & Triage API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten via env in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(analyze.router, prefix="/analyze", tags=["analyze"])
app.include_router(integrate.router, prefix="/integrate", tags=["integrations"])

@app.get("/healthz")
def healthz():
    return {"ok": True}