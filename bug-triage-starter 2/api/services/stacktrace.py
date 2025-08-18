# Placeholder heuristics; expand with language detection and patterns
def analyze(trace: str | None) -> dict:
    if not trace:
        return {}
    hints = []
    if "TypeError" in trace:
        hints.append("Check null/undefined guards and API response shape.")
    if "KeyError" in trace:
        hints.append("Reproduce with a payload missing the referenced key.")
    return {"hints": hints}