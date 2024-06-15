from pydantic import BaseModel


class AuthSettings(BaseModel):
    setting1: str = "auth_setting_1"

