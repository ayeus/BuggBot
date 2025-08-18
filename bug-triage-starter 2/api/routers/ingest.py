from fastapi import APIRouter
from models.schemas import BugIn
from services import nlp as nlp_service
from services import priority as priority_service
from services import stacktrace as stx_service
from services import owner as owner_service
from services import repro as repro_service

router = APIRouter()

@router.post("/manual")
def ingest_manual(bug: BugIn):
    # Minimal "analyze now" flow for MVP
    parsed = nlp_service.parse_report(bug)
    priority = priority_service.classify_priority(bug, parsed)
    owner = owner_service.resolve_owner(parsed)
    artifacts = repro_service.generate(parsed)
    return {
        "parsed": parsed,
        "priority": priority,
        "owner": owner,
        "artifacts": artifacts,
    }