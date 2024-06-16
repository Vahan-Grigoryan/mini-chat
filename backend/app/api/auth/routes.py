"""
Path operations
"""
from typing_extensions import Annotated
from fastapi import APIRouter, Depends
from core import dependencies as global_deps


router = APIRouter()


@router.get("/register")
def register_user(
    settings: global_deps.settings,
    db_session: global_deps.db_session,
):
    return "Not implemented"

@router.get("/login")
def login_user(
    settings: global_deps.settings,
    db_session: global_deps.db_session,
):
    return "Not implemented"

