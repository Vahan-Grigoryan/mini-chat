from sqlalchemy import Boolean, Column, ForeignKey, Index, String, Table, Text
from sqlalchemy.orm import relationship
from core.db import Base


conversations_users_associations = Table(
    "conversations_users_associations",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("conversation_id", ForeignKey("conversations.id")),
)

class Conversation(Base):
    """Conversation model for storing group messages between users"""
    name = Column(String(200), nullable=False)
    photo = Column(Text)
    private = Column(Boolean, default=True) # True if conversation between 2 users only
    admin_id = Column(ForeignKey("users.id"))
    admin = relationship("User", back_populates="admin_in_conversations")
    group_messages = relationship(
        "GroupMessage",
	    back_populates="conversation"
    )
    users = relationship(
        "User",
	    conversations_users_associations,
	    back_populates="conversations"
    )

    __table_args__ = (
        # conversations with private=False must have unique name between themselves
        Index(
            "public_convs_are_unique",
            "name",
            unique=True,
            postgresql_where=("not private")
        ),
    )


class GroupMessage(Base):
    """
    Users can send only group of
    messages(which will contain >= 1 messages) to each other.
    This is the db table for it.
    """
    messages = relationship("Message", back_populates="group_message")
    conversation_id = Column(ForeignKey("conversations.id"), nullable=False)
    conversation = relationship("Conversation", back_populates="group_messages")
    author_id = Column(ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="group_messages")


class Message(Base):
    """Messages model"""
    text = Column(String)
    images = relationship("Image", back_populates="message")
    group_message_id = Column(ForeignKey("group_messages.id"), nullable=False)
    group_message = relationship("GroupMessage", back_populates="messages")
    linking_message_id = Column(ForeignKey("messages.id"))
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
    message = relationship("Message", back_populates="images")

