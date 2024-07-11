"""
Dependencies for path operations.
Dependencies starting with the underscore are intended for a valid alias of type.
"""
import re
from fastapi import Depends, File, Form, HTTPException, UploadFile
from typing_extensions import Annotated
from . import models, utils
from core import dependencies as global_deps
from email_validator import validate_email, EmailNotValidError


def check_email(
    email: Annotated[str, Form()],
):
    """
    Validate email.
    Return it if valid, else raise error
    """
    try:
        emailinfo = validate_email(email)
        return emailinfo.normalized
    
    except EmailNotValidError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "field": "email",
                "message": str(e)
            }
        )


def check_password(
    password: Annotated[str, Form(min_length=8, max_length=200)],
):
    """
    Ensures that password contain 
    minimal required valid characters.
    Return it if valid, else raise error
    """
    match = re.search(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).+$", password)

    if match: return password

    raise HTTPException(
        status_code=400,
        detail={
            "field": "password",
            "message": "Password should have at least 1 number, 1 lowercase letter, 1 uppercase letter"
        }
    )

async def _create_user(
    db_session: global_deps.db_session,

    email: Annotated[str, Depends(check_email)],
    first_name: Annotated[str, Form(min_length=2, max_length=50)],
    last_name: Annotated[str, Form(min_length=2, max_length=50)],
    password: Annotated[str, Depends(check_password)],
    age: Annotated[int | None, Form(gt=5)] = None,
    photo: Annotated[UploadFile | None, File()] = None,
    tel: Annotated[int | None, Form()] = None,
):
    """Create and return user."""
    user = models.User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        age=age,
        tel=tel
    )
    user.set_password(password)
    db_session.add(user)
    db_session.flush()
    photo_image_path = await utils.download_photo_if_provided(photo, user.id)
    user.photo = photo_image_path or None

    return user
    

create_user = Annotated[models.User, Depends(_create_user)]
