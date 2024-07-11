"""There are all sub dependencies"""

import re
from fastapi import Form, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from typing_extensions import Annotated
from . import models, schemas
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
        emailinfo = validate_email(email, check_deliverability=True)
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

