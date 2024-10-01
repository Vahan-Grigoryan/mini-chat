from fastapi import APIRouter, Response
from api.auth.dependencies import current_user
from core.dependencies import db_session
from . import schemas, db_manipulations, dependencies


router = APIRouter()


@router.get(
    "/search_conversations_and_users",
    response_model=list[schemas.ConversationScheme | schemas.UserMiniInfo]
)
def search_conversations_and_users(
    db_session: db_session,
    keyword: str
):
    """Search conversations and users"""
    return db_manipulations.find_conversations_and_users(
        db_session,
        keyword
    )


@router.get(
    "/conversations/mine",
    response_model=list[schemas.ConversationScheme]
)
def get_user_conversations(user: current_user):
    """Receive all conversations of user"""
    return user.conversations


@router.get(
    "/conversations/{conversation_id}",
    response_model=schemas.ConversationDetailScheme
)
def get_conversation(
    db_session: db_session,
    conversation_id: int
):
    """Get conversation detail info"""
    return db_manipulations.get_conversation(db_session, conversation_id)


@router.post(
    "/conversations",
    response_model=schemas.ConversationScheme
)
def create_conversation(
    conversation: dependencies.create_conversation
):
    return conversation


@router.patch(
    "/conversations/{conversation_id}",
)
def alter_conversation(
    altered_conversation: dependencies.alter_conversation
):
    return altered_conversation


@router.delete(
    "/conversations/{conversation_id}",
)
def delete_conversation(
    db_session: db_session,
    _: current_user,
    conversation_id: int
):
    db_manipulations.del_conversation(
        db_session,
        conversation_id
    )
    return Response(status_code=201)


@router.post(
    "/conversations/{conversation_id}/users/{user_id}",
)
def add_user_to_conversation(
    is_added: dependencies.add_user_to_conversation
):
    if is_added:
        return Response(status_code=201)
    else:
        return Response(
            "You haven't enough permissions to add users to this conversation",
            status_code=403
        )


@router.delete(
    "/conversations/{conversation_id}/users/{user_id}",
)
def del_user_from_conversation(
    is_deleted: dependencies.del_user_from_conversation
):
    if is_deleted:
        return Response(status_code=200)
    else:
        return Response(status_code=422)
