
from fastapi import FastAPI
from .db.dao import get_engine, init_db
from .routers import ingest, analyze, integrate

app = FastAPI(title="BuggBit API", version="0.1.0")

@app.on_event("startup")
def _startup():
    engine = get_engine()
    init_db(engine)

app.include_router(ingest.router)
app.include_router(analyze.router)
app.include_router(integrate.router)

@app.get("/healthz")
def healthz():
    return {"status":"ok"}
