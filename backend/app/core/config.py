"""
Settings for whole project
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, computed_field


class DatabaseSettings(BaseModel):
    drivername: str | None = None
    username: str | None = None
    password: str | None = None
    host: str | None = None
    database: str | None = None
    

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_nested_delimiter="__")

    host: str = "localhost"
    port: int = 8000

    db: DatabaseSettings
    #auth: AuthSettings

    @computed_field
    @property
    def uri(self) -> str:
        return f"http://{self.host}:{self.port}"
