from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=Token)
def login(username: str, password: str):
    # MVP-only, replace with GitHub OAuth later
    return Token(access_token="dev-token")