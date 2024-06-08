from functools import lru_cache
from typing_extensions import Annotated
from .config import AuthSettings
from fastapi import APIRouter, Depends


router = APIRouter()

@lru_cache
def get_settings():
    return AuthSettings()

dependent_settings = Annotated[AuthSettings, Depends(get_settings)]

@router.get("/register")
def register_user(settings: dependent_settings):
    return "Not implemented"

@router.get("/login")
def login_user(settings: dependent_settings):
    return "Not implemented"

