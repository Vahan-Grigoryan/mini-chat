"""
Request bodies for path operations
"""
from pydantic import BaseModel, ConfigDict


class UserRegistrationResponse(BaseModel):
    """Model used for returning created user"""
    model_config = ConfigDict(from_attributes=True)

    email: str
    first_name: str
    last_name: str
    age: int | None
    photo: str | None
    tel: str | None
