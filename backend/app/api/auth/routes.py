"""
Path operations
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.auth import utils
from core import dependencies as global_deps
from . import dependencies, schemas


router = APIRouter()


@router.post(
    "/register",
    response_model=schemas.UserDataResponse
)
async def register_user(
    created_user: dependencies.create_user,
):
    """User registration endpoint"""

    return created_user


@router.post("/tokens")
def tokens(
    user: dependencies.authenticate_user,
    settings: global_deps.settings
):
    """
	Create pair tokens, 
    return access_token and it's type in response body,
    return refresh_token as httponly cookie
	"""
    access_token = utils.create_token(
        "access_token",
        {"user_id": user.id},
        settings
    )
    refresh_token = utils.create_token(
        "refresh_token",
        {"user_id": user.id},
        settings
    )
    response = JSONResponse(
        {"access_token": access_token, "token_type": "Bearer"}
    )
    response.set_cookie(
        "refresh_token",
        refresh_token,
        settings.auth.jwt_refresh_token_lifetime*60,
        httponly=True
    )
    return response


@router.get("/users/me", response_model=schemas.UserDataResponse)
def route_with_required_auth(current_user: dependencies.current_user):
    """Just check valid auth in this path operation(temporary)"""
    return current_user
