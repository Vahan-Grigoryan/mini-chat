"""
There are all db manipulations(CRUD and other functionality)
"""

from sqlalchemy import select, exc
from sqlalchemy.orm import Session
from . import models, utils


async def create_user(db_session: Session, user_credentials: dict):
    """
	Create user with given credentials
	"""
    password = user_credentials.pop("password")
    photo = user_credentials.pop("photo")
    user = models.User(**user_credentials)
    user.set_password(password)
    db_session.add(user)
    db_session.flush() # flush() need for ensure email uniqueness before setting photo
    photo_image_path = await utils.download_photo_if_provided(photo, user.id)
    user.photo = photo_image_path
    return user


def get_user(db_session: Session, search_fields: dict):
    """Find user by search_fields and return it or none"""
    return db_session.execute(
        select(models.User)
        .filter_by(**search_fields)
    ).scalar_one_or_none()
