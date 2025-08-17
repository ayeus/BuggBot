
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class IngestManual(BaseModel):
    title: str
    description: Optional[str] = None
    stack_trace: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class AnalyzeRequest(BaseModel):
    bug_id: Optional[int] = None

class BugRecord(BaseModel):
    id: int
    priority: str
    assigned_to: Optional[str] = None
    module_guess: Optional[str] = None
    environment: Optional[dict] = None
    status: str
