from fastapi import APIRouter

router = APIRouter()

@router.post("/github/comment")
def github_comment(bug_id: int):
    # TODO: implement
    return {"status": "queued", "bug_id": bug_id}