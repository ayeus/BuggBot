
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_debug: bool = True
    api_secret_key: str = "change-me"

    mysql_host: str = "localhost"
    mysql_port: int = 3307
    mysql_user: str = "buggbit"
    mysql_password: str = "buggbitpwd"
    mysql_db: str = "buggbit"

    class Config:
        env_file = "infra/.env"

settings = Settings()
