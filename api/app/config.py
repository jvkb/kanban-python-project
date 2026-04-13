from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    openai_api_key: str

    model_config = {"env_file": ".env"}


settings = Settings()
