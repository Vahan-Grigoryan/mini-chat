from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from core.db import Base


conversations_and_users_associations = Table(
    "conversations_and_users_associations",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("conversation_id", ForeignKey("conversations.id")),
)

class Conversation(Base):
    """Conversation model for storing group messages between users"""
    users = relationship(
        "User",
	    conversations_and_users_associations,
	    back_populates="conversations"
    )


class GroupMessage(Base):
    """
    Users can send only group of
    messages(which will contain >= 1 messages) to each other.
    This is the db table for it.
    """
    author_id = Column(ForeignKey("users.id"), nullable=False)
    author = relationship("User")


class Message(Base):
    """Messages model"""
    text = Column(String)
    linking_message_id = Column(ForeignKey("messages.id"))
    group_message_id = Column(ForeignKey("group_messages.id"), nullable=False)
    group_message = relationship("GroupMessage")
    linking_message = relationship("Message")

    @property
    def author(self):
        """Author field for showing he in linking message"""
        return self.group_message.author


class Image(Base):
    """Image table for images in messages with optional description"""
    path = Column(String, nullable=False)
    desc = Column(String)
    message_id = Column(ForeignKey("messages.id"), nullable=False)
    message = relationship("Message")

