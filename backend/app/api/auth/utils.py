"""
This file contains functions that may will be used in many places in this service.
DRY pattern.
"""
from datetime import datetime, timedelta, timezone
from typing import Literal
import jwt
from fastapi import UploadFile
from core.config import Settings


async def download_photo_if_provided(
    photo: UploadFile | None,
    user_id: int,
):
    """
    Create/change photo image if provided,
    return photo path or None
    """
    if not photo: return 

    photo_path = f"images/photo_for_user_{user_id}.{photo.filename.split('.')[-1]}"
    
    with open(photo_path, "wb") as f:
        f.write(await photo.read())

    return photo_path

def create_token(
    token_name: Literal["access_token", "refresh_token"],
	payload_part: dict,
	settings: Settings
):
    """
	Create token and return it
	"""
    if token_name == "access_token":
        token_lifetime = timedelta(minutes=settings.auth.jwt_access_token_lifetime)
    else:
        token_lifetime = timedelta(minutes=settings.auth.jwt_refresh_token_lifetime)

    token = jwt.encode(
        {
            "token_name": token_name, 
	        "exp": datetime.now(timezone.utc) + token_lifetime,
            **payload_part
        },
        settings.secret_key,
        settings.auth.jwt_algorithm,
        headers={"typ":"Bearer"}
    )

    return token
