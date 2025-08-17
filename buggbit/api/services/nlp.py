
import re
from typing import Dict, Any, Optional

_OS = re.compile(r'(Windows\s?(\d+|11)|iOS\s?\d+|Android\s?\d+|Ubuntu\s?\d+)', re.I)
_BROWSER = re.compile(r'(Chrome|Safari|Firefox)\s?\d+', re.I)
_JS_TYPEERROR = re.compile(r'TypeError:', re.I)
_PY_TRACE = re.compile(r'Traceback \(most recent call last\):', re.I)
_JS_STACK = re.compile(r'\sat\s.+\(.+\.js:\d+:\d+\)', re.I)

def parse_env(title: str, description: Optional[str], stack_trace: Optional[str]) -> Dict[str, Any]:
    blob = " ".join([x for x in [title, description or '', stack_trace or ''] if x])
    os_m = _OS.search(blob)
    br_m = _BROWSER.search(blob)
    env = {}
    if os_m:
        env["os"] = os_m.group(0)
    if br_m:
        env["browser"] = br_m.group(0)
    return env

def detect_error_type(stack_trace: Optional[str]) -> Optional[str]:
    if not stack_trace:
        return None
    if _PY_TRACE.search(stack_trace):
        return "PythonTraceback"
    if _JS_TYPEERROR.search(stack_trace) or _JS_STACK.search(stack_trace):
        return "JSTypeError"
    return None
