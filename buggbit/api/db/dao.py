
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from .config import settings

def get_engine() -> Engine:
    url = f"mysql+pymysql://{settings.mysql_user}:{settings.mysql_password}@{settings.mysql_host}:{settings.mysql_port}/{settings.mysql_db}"
    engine = create_engine(url, pool_pre_ping=True, pool_recycle=3600)
    return engine

def init_db(engine: Engine):
    with engine.connect() as conn:
        with open('api/db/schema.sql','r',encoding='utf-8') as f:
            conn.execute(text(f.read()))
        conn.commit()
