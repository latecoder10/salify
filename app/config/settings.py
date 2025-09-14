from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App settings
    app_name: str = "Sales AI Assistant"
    app_version: str = "1.0.0"
    app_env: str = "development"

    # Database settings
    db_user: str = "your_db_user"
    db_password: str = "your_db_password"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "your_db_name"

    # Security settings
    secret_key: str = "your_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }


settings = Settings()
