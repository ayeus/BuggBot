
from typing import Optional, Dict

# seeded module -> owner map (extend in DB later)
SEED_MAP: Dict[str, str] = {
    "auth": "aayush",
    "payments": "priyanka",
    "search": "rohan",
}

def resolve_owner(module_guess: Optional[str]) -> Optional[str]:
    if not module_guess:
        return None
    prefix = module_guess.split('/')[0]
    return SEED_MAP.get(prefix)
