"""
This file contains functions that will be used in many places in this service.
DRY pattern.
"""
from fastapi import UploadFile


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
