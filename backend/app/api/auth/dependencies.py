"""
Dependencies for path operations.
Dependencies starting with the underscore are intended for a valid alias of type.
"""
import re, jwt
from fastapi import Depends, File, Form, HTTPException, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select, exc
from typing_extensions import Annotated
from . import models, sub_dependencies, db_manipulations
from core import dependencies as global_deps


async def _create_user(
    db_session: global_deps.db_session,
    email: Annotated[str, Depends(sub_dependencies.check_email)],
    first_name: Annotated[str, Form(min_length=2, max_length=50)],
    last_name: Annotated[str, Form(min_length=2, max_length=50)],
    password: Annotated[str, Depends(sub_dependencies.check_password)],
    photo: Annotated[UploadFile | None, File()] = None,
    age: Annotated[int | None, Form(gt=5)] = None,
    tel: Annotated[int | None, Form()] = None,
):
    """Create and return user to path operation"""
    try:
        user = await db_manipulations.create_user(
            db_session,
            {
                "email": email,
                "password": password,
                "photo": photo,
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "tel": tel,
            }
        )
    except exc.IntegrityError as e:
        # if any error will occur
        # while creating user in db(email uniqueness violation for example),
        # it will be shown to user
        error_string = re.sub(
            r"\(|\)|DETAIL:  |Key ",
            '',
            str(e.orig).split('\n')[-2]
        )
        raise HTTPException(
            status_code=400,
            detail={
                "message": error_string
            }
        )

    return user


def _get_current_user(
    db_session: global_deps.db_session,
    settings: global_deps.settings,
    access_token: Annotated[str,
        Depends(OAuth2PasswordBearer(tokenUrl="tokens"))
    ]
):
    """
    Find and return user by provided access_token in header.
    If access_token expired, raise appropriate error.
    If unexpected error occured, return it to client
    """
    try:
        payload = jwt.decode(
            access_token,
	        settings.secret_key,
	        [settings.auth.jwt_algorithm]
        )
        return db_manipulations.get_user(db_session, {"id": payload["user_id"]})
        
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail={
                "message": "Access token expired"
            }
        )

    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Something went wrong"
            }
        )


def _authenticate_user(
    db_session: global_deps.db_session,
    user_credetnials: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    Find user by email(username in OAuth2PasswordRequestForm)
    and check password, if it invalid, raise error,
    else return found user
    """
    user = db_manipulations.get_user(
        db_session,
	    {"email": user_credetnials.username}
    )
    if not user or not user.check_password(user_credetnials.password):
        raise HTTPException(
            status_code=401,
            detail={
                "message": "Invalid email or password"
            }
        )

    return user


authenticate_user = Annotated[models.User, Depends(_authenticate_user)]
create_user = Annotated[models.User, Depends(_create_user)]
current_user = Annotated[models.User, Depends(_get_current_user)]
