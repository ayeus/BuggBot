from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class BugIn(BaseModel):
    title: str
    description: str
    stack_trace: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class BugOut(BugIn):
    id: int
    priority: Optional[str] = None
    severity: Optional[str] = None
    assigned_to: Optional[str] = None
    environment: Optional[Dict[str, Any]] = None
    module_guess: Optional[str] = None
    error_type: Optional[str] = None
    repro_steps: Optional[str] = None
    repro_script: Optional[str] = None
    dockerfile: Optional[str] = None