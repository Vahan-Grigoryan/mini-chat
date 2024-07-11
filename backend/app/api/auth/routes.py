"""
Path operations
"""
from fastapi import APIRouter
from . import dependencies, schemas


router = APIRouter()


@router.post(
    "/register",
	response_model=schemas.UserRegistrationResponse
)
async def register_user(
    created_user: dependencies.create_user,
):
    """User registration endpoint"""

    return created_user

@router.get("/login")
def login_user():
    return "Not implemented"

