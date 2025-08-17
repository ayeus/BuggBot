
from fastapi import APIRouter

router = APIRouter(prefix="/integrate", tags=["integrations"])

@router.post("/github/push")
def github_push(bug_id: int):
    # TODO: implement GitHub Issues comment with triage summary
    return {"ok": True, "bug_id": bug_id}

@router.post("/jira/push")
def jira_push(bug_id: int):
    # TODO: implement Jira update/create
    return {"ok": True, "bug_id": bug_id}
