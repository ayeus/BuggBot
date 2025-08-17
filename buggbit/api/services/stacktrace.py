
from typing import Optional

def guess_module_from_stack(stack_trace: Optional[str]) -> Optional[str]:
    if not stack_trace:
        return None
    # naive: extract path-like tokens to guess module
    for token in stack_trace.split():
        if '/' in token and ('.py' in token or '.ts' in token or '.js' in token or '.java' in token):
            return token.split('/')[0]
    return None
