from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    host: str = "localhost"
    port: int = 8000
