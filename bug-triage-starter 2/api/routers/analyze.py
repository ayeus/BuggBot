from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def analyze_run(bug_id: int | None = None):
    # Placeholder: would load by bug_id or latest bug and analyze
    return {"status": "ok", "bug_id": bug_id}