# MVP: static map; extend with Git blame + path prefixes.
MODULE_MAP = {
    "/auth/frontend": "aayush",
    "/payments/api": "priyanka",
    "/search/index": "rohan",
}

def resolve_owner(parsed: dict) -> str | None:
    module = parsed.get("module_guess")
    if module and module in MODULE_MAP:
        return MODULE_MAP[module]
    return "triage@team"