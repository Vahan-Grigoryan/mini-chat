import random
from fastapi import UploadFile
from fastapi.exceptions import HTTPException
from sqlalchemy import exc, insert, not_, select, or_
from sqlalchemy.orm import selectinload
from api.auth.models import User
from api.auth.db_manipulations import get_user
from core import utils
from . import models, schemas


def find_conversations_and_users(
    db_session,
    keyword: str
) -> list[models.Conversation | User]:
    """Find conversations and users by same keyword"""

    _keyword = keyword.lower()
    conversations = select(models.Conversation).where(
        models.Conversation.name.contains(_keyword),
        not_(models.Conversation.private)
    )
    users = select(User).where(
        or_(
            User.first_name.contains(_keyword),
            User.last_name.contains(_keyword)
        )
    )
    result = db_session.execute(conversations).scalars().all()
    result += db_session.execute(users).scalars().all()
    return result

async def create_private_conversation(
    db_session,
    user: User,
    photo: UploadFile | None,
    first_included_user_id: int,
) -> models.Conversation:
    """
    Create private conversation for authorized user
    with first companion found by first_included_user_id
    """

    first_user = get_user(db_session, {"id": first_included_user_id})
    if first_user is None:
        raise HTTPException(404, "First companion in conversation not found")

    conversation = models.Conversation(
        name=f"{first_user.first_name} {first_user.last_name}",
        admin_id=user.id,
        private=True,
    )
    
    conversation.users = [user, first_user]
    db_session.add(conversation)
    db_session.flush()
    conversation.photo = await utils.download_photo_if_provided(
        photo,
    	conversation_id=conversation.id
    )
    return conversation

async def create_not_private_conversation(
    db_session,
    user: User,
    photo: UploadFile | None,
    conversation_name: str,
) -> models.Conversation:
    """
    Create not private conversation for authorized user
    with name conversation_name and with only
    creator himself included in conversation
    """

    # there may be IntegrityError for conversation name column,
    # (which have unique conditional index in db)
    # if any, this error must be handled by dependency 
    try:
        conversation = models.Conversation(
            name=conversation_name,
            admin_id=user.id,
            private=False
        )
        db_session.add(conversation)
        db_session.flush()
    except exc.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Conversation with this name already exists"
            }
        )

    conversation.photo = await utils.download_photo_if_provided(
        photo,
    	conversation_id=conversation.id
    )
    conversation.users = [user]
    return conversation


async def alter_conversation(
    db_session,
	user: User,
	conversation_id: int,
	altering_data: schemas.AlterConversationData
):
    conversation = db_session.get(models.Conversation, conversation_id)

    if user not in conversation.users:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "You are not member of this conversation"
            }
        )

    print(altering_data.photo, conversation_id)
    if altering_data.conversation_name:
        conversation.name = altering_data.conversation_name
    elif altering_data.photo:
        conversation.photo = await utils.download_photo_if_provided(
            altering_data.photo,
            conversation_id=conversation.id
        )
    elif altering_data.admin_id and conversation.admin_id == user.id:
        conversation.admin_id = altering_data.admin_id

    return conversation

def del_conversation(
    db_session,
	conversation_id: int
):
    conversation = db_session.get(models.Conversation, conversation_id)
    db_session.delete(conversation)


def get_conversation(
    db_session,
    conversation_id: int
) -> models.Conversation | None:
    """Get one conversation by id"""

    return db_session.execute(
        select(models.Conversation).
        options(selectinload(models.Conversation.users)).
        filter_by(id = conversation_id)
    ).scalar_one_or_none()


def add_user_to_conversation(
    db_session,
    user: User,
    conversation_id: int,
    new_user_id: int
) -> bool:
    """
    Add new companion to conversation
    if user who adds is admin
    """

    conversation = db_session.get(models.Conversation, conversation_id)
    if conversation.admin_id != user.id:
        return False

    db_session.add(conversation)
    db_session.execute(
        insert(models.conversations_users_associations).
        values(user_id=new_user_id, conversation_id=conversation_id)
    )
    return True

def del_user_from_conversation(
    db_session,
    user: User,
    conversation_id: int,
    extra_user_id: int
) -> bool:
    """
    Del extra user from conversation and
    return true if deleted and false if not.

    1)  If conversation is private, and user try to delete
        other companion, regardless admin privileges,
        conversation will be deleted
    2)  If user who deletes is admin and he deletes himself,
        set admin any other user from conversation and deletes his
    3)  Same as point 2, but user haven't admin privileges and
        admin keeps same
    4)  If conversation is not private and admin tries
        to remove other user(not himself), just remove extra user
    5)  If user who isn't admin tries to remove other user from
        not private conversation, return false.

    LAST CASE IS FOR INCREASING SECURITY,
    assumed that js can't do similar request,
    that case may changed in future
    """
    conversation = db_session.get(models.Conversation, conversation_id)
    extra_user = db_session.get(User, extra_user_id)

    if conversation.private:
        db_session.delete(conversation)
    elif user.id == extra_user_id == conversation.admin_id:
        random_user_from_conversation = random.choice(conversation.users)
        conversation.admin = random_user_from_conversation
        conversation.users.remove(extra_user)
    elif user.id == extra_user_id:
        conversation.users.remove(extra_user)
    elif not conversation.private and conversation.admin_id == user.id:
        conversation.users.remove(extra_user)
    elif not conversation.private and conversation.admin_id != user.id:
        return False

    return True
