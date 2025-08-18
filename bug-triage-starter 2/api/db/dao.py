import os
from sqlalchemy import create_engine, text

def _url():
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    user = os.getenv("DB_USER", "bugtriage")
    pwd = os.getenv("DB_PASSWORD", "bugtriage")
    db = os.getenv("DB_NAME", "bugtriage")
    return f"postgresql+psycopg://{user}:{pwd}@{host}:{port}/{db}"

engine = create_engine(_url(), future=True)

def init_db():
    with engine.connect() as conn:
        schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.execute(text(f.read()))
        conn.commit()