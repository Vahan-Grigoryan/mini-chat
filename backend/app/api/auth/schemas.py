"""
Request bodies for path operations
"""
from pydantic import BaseModel, ConfigDict


class UserDataResponse(BaseModel):
    """
    Model used for returning full user data
    (can be used after creating/finding/updating user)
    """
    model_config = ConfigDict(from_attributes=True)

    email: str
    first_name: str
    last_name: str
    age: int | None
    photo: str | None
    tel: str | None


class AccessToken(BaseModel):
    access_token: str
    token_type: str
