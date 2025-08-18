import json, os, re
from models.schemas import BugIn

def _rules_path():
    return os.getenv("PRIORITY_RULES", "/app/data/rules/priority.json")

def classify_priority(bug: BugIn, parsed: dict) -> str:
    try:
        with open(_rules_path(), "r", encoding="utf-8") as f:
            rules = json.load(f)
    except Exception:
        rules = []
    text = f"{bug.title}\n{bug.description}\n{bug.stack_trace or ''}"
    for r in rules:
        if re.search(r.get("pattern",""), text, flags=re.I):
            return r.get("priority", "P2")
    return "P2"