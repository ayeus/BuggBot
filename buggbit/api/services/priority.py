
import json, re
from pathlib import Path

DEFAULT_RULES = [
    {"pattern": "(data loss|security|payment|login|auth)", "priority": "P0"},
    {"pattern": "(crash|not responding|freeze)", "priority": "P0"},
    {"pattern": "(slow|timeout|incorrect|broken)", "priority": "P1"},
    {"pattern": "(ui|typo|alignment)", "priority": "P2"},
]

def load_rules(path: str = "data/rules/priority.json"):
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    return DEFAULT_RULES

def rule_based_priority(text: str, rules=None) -> str:
    rules = rules or load_rules()
    for r in rules:
        if re.search(r["pattern"], text, flags=re.I):
            return r["priority"]
    return "P2"
