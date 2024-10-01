from dataclasses import dataclass
from typing import Annotated
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, ConfigDict


class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserMiniInfo(OrmBaseModel):
    id: int
    first_name: str
    last_name: str
    photo: str | None


class ImageScheme(OrmBaseModel):
    path: str
    desc: str | None


class MessageScheme(OrmBaseModel):
    text: str | None
    images: list[ImageScheme] | None
    author: UserMiniInfo | None
    linking_message: "MessageScheme | None"
    group_message: "GroupMessage"


class GroupMessage(OrmBaseModel):
    conversation: "ConversationScheme"
    author: UserMiniInfo


class ConversationScheme(OrmBaseModel):
    name: str
    photo: str | None


class ConversationDetailScheme(ConversationScheme):
    users: list[UserMiniInfo]


@dataclass(slots=True)
class ConversationExtendableData():
    conversation_name: Annotated[str | None, Form()] = None
    photo: Annotated[UploadFile | None, File()] = None


@dataclass(slots=True)
class CreateConversationData(ConversationExtendableData):
    is_private: Annotated[bool, Form()] = True
    first_included_user_id: Annotated[int | None, Form()] = None


@dataclass(slots=True)
class AlterConversationData(ConversationExtendableData):
    admin_id: Annotated[int | None, Form()] = None
