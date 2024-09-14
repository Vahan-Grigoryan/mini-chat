"""
Models(db tables)
"""
import hashlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base
from api.chat.models import conversations_and_users_associations


class User(Base):
    """User model"""

    email = Column(String(500), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    age = Column(Integer)
    photo = Column(String(500))
    tel = Column(Integer)

    conversations = relationship(
        "Conversation",
    	conversations_and_users_associations,
    	back_populates="users"
    )

    def set_password(self, new_password):
        h = hashlib.sha512(bytes(new_password, encoding="utf-8"))
        self.password = h.hexdigest()

    def check_password(self, password):
        h = hashlib.sha512(bytes(password, encoding="utf-8"))
        return self.password == h.hexdigest()
