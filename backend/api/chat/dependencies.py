from typing import Annotated
from fastapi import Depends, HTTPException
from api.auth.dependencies import current_user
from core.dependencies import db_session
from . import db_manipulations, models, schemas


async def _create_conversation(
    db_session: db_session,
    user: current_user,
    creation_data: schemas.CreateConversationData = Depends()
) -> models.Conversation:
    """Create private or not private conversation"""

    if creation_data.is_private and creation_data.first_included_user_id:
        return await db_manipulations.create_private_conversation(
            db_session,
        	user,
            creation_data.photo,
        	creation_data.first_included_user_id
        )
    elif not creation_data.is_private and creation_data.conversation_name:
        return await db_manipulations.create_not_private_conversation(
            db_session,
            user,
            creation_data.photo,
            creation_data.conversation_name
        )
    else:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Provide one of (first_included_user_id, conversation_name) fields"
            }
        )


async def _alter_conversation(
    db_session: db_session,
	user: current_user,
	conversation_id: int,
	altering_data: schemas.AlterConversationData = Depends()
):
    return await db_manipulations.alter_conversation(
        db_session,
    	user,
    	conversation_id,
    	altering_data
    )


def _add_user_to_conversation(
    db_session: db_session,
    user: current_user,
    conversation_id: int,
    user_id: int
) -> bool:

    return db_manipulations.add_user_to_conversation(
        db_session,
        user,
        conversation_id,
        user_id
    )
    
def _del_user_from_conversation(
    db_session: db_session,
    user: current_user,
    conversation_id: int,
    user_id: int
) -> bool:

    return db_manipulations.del_user_from_conversation(
        db_session,
        user,
        conversation_id,
        user_id
    )



create_conversation = Annotated[
    models.Conversation,
    Depends(_create_conversation)
]
alter_conversation = Annotated[models.Conversation, Depends(_alter_conversation)]
add_user_to_conversation = Annotated[bool, Depends(_add_user_to_conversation)]
del_user_from_conversation = Annotated[bool, Depends(_del_user_from_conversation)]
