def generate(parsed: dict) -> dict:
    # For MVP, return simple artifacts; fill from templates later.
    dockerfile = "FROM node:18\n# ... see docker/templates for full examples"
    steps_md = "# Reproduction Steps\n1. Open app\n2. Click login\n3. Observe error"
    run_sh = "#!/usr/bin/env bash\necho 'Run repro script'"
    return {
        "dockerfile": dockerfile,
        "steps.md": steps_md,
        "run.sh": run_sh
    }