
from fastapi import APIRouter
from ..models.schemas import IngestManual
from ..services import nlp, priority, stacktrace, owner, repro
from ..db.dao import get_engine
from sqlalchemy import text

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/manual")
def ingest_manual(payload: IngestManual):
    engine = get_engine()
    env = nlp.parse_env(payload.title, payload.description, payload.stack_trace)
    err_type = nlp.detect_error_type(payload.stack_trace)
    module_guess = stacktrace.guess_module_from_stack(payload.stack_trace)
    pri = priority.rule_based_priority(" ".join([payload.title, payload.description or ""]))
    assignee = owner.resolve_owner(module_guess)

    artifacts = repro.generate_artifacts(env, scenario=err_type or "default")

    with engine.begin() as conn:
        res = conn.execute(text("""
            INSERT INTO bugs (source, title, description, stack_trace, environment, module_guess, priority, assigned_to, repro_steps, repro_script, dockerfile)
            VALUES (:source, :title, :description, :stack_trace, CAST(:environment AS JSON), :module_guess, :priority, :assigned_to, :repro_steps, :repro_script, :dockerfile)
        """), {
            "source": "manual",
            "title": payload.title,
            "description": payload.description,
            "stack_trace": payload.stack_trace,
            "environment": json.dumps(env),
            "module_guess": module_guess,
            "priority": pri,
            "assigned_to": assignee,
            "repro_steps": artifacts["steps_md"],
            "repro_script": artifacts["run_sh"],
            "dockerfile": artifacts["dockerfile"],
        })
        bug_id = res.lastrowid

    return {"bug_id": bug_id, "priority": pri, "assigned_to": assignee, "env": env, "module_guess": module_guess}
