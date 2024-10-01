from sqlalchemy import select
from . import models
from core import utils


async def create_user(db_session, user_credentials: dict) -> models.User:
    """Create user with given credentials"""
    password = user_credentials.pop("password")
    photo = user_credentials.pop("photo")
    user = models.User(**user_credentials)
    user.set_password(password)
    db_session.add(user)
    db_session.flush() # flush() need for ensure email uniqueness before setting photo
    photo_image_path = await utils.download_photo_if_provided(
        photo,
    	user_id=user.id
    )
    user.photo = photo_image_path
    return user


def get_user(db_session, search_fields: dict) -> models.User | None:
    """Find user by search_fields and return it or None"""
    return db_session.execute(
        select(models.User)
        .filter_by(**search_fields)
    ).scalar_one_or_none()
