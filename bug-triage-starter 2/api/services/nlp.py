from typing import Dict, Any
from models.schemas import BugIn
import re

OS_PAT = re.compile(r'(Windows\s?(\d+|11)|iOS\s?\d+|Android\s?\d+|Ubuntu\s?\d+)', re.I)
BROWSER_PAT = re.compile(r'(Chrome|Safari|Firefox)\s?\d+', re.I)
JS_TYPEERROR = re.compile(r'TypeError', re.I)

def parse_report(bug: BugIn) -> Dict[str, Any]:
    text = f"{bug.title}\n{bug.description}\n{bug.stack_trace or ''}"
    env = {}
    if (m := OS_PAT.search(text)):
        env['os'] = m.group(0)
    if (m := BROWSER_PAT.search(text)):
        env['browser'] = m.group(0)
    error_type = 'TypeError' if JS_TYPEERROR.search(text) else None
    module_guess = None  # left for owner resolver or path regex
    return {
        "env": env or None,
        "error_type": error_type,
        "module_guess": module_guess
    }