
from typing import Dict

def generate_artifacts(env: Dict, scenario: str = "default") -> Dict[str, str]:
    dockerfile = f"""FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV BUG_SCENARIO="{scenario}"
CMD ["bash","run.sh"]
"""
    run_sh = """#!/usr/bin/env bash
set -euo pipefail
export NODE_ENV=test
# TODO: start services, run automated repro (e.g., Playwright)
echo "Reproducing scenario: $BUG_SCENARIO"
"""
    steps_md = f"""# Reproduction Steps
1. Start services
2. Execute automated steps for scenario: {scenario}
3. Observe error in logs/console
"""
    return {"dockerfile": dockerfile, "run_sh": run_sh, "steps_md": steps_md}
