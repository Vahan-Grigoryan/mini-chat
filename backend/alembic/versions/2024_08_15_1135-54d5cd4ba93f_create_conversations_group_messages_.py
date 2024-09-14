"""
Create conversations, group_messages, messages, images tables

Revision ID: 54d5cd4ba93f
Revises: 6317a41559b7
Create Date: 2024-08-15 11:35:02.369579

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54d5cd4ba93f'
down_revision: str | None = '6317a41559b7'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "conversations",
        sa.Column("id", sa.Integer, primary_key=True),
    )
    op.create_table(
        "group_messages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "author_id",
	        sa.Integer,
	        sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False
        ),
        sa.Column(
            "conversation_id",
	        sa.Integer,
	        sa.ForeignKey("conversations.id", ondelete="CASCADE"),
            nullable=False
        ),
    )
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.Text),
        sa.Column(
            "linking_message_id",
	        sa.Integer,
	        sa.ForeignKey("messages.id", ondelete="CASCADE")
        ),
        sa.Column(
            "group_message_id",
            sa.Integer,
            sa.ForeignKey("group_messages.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    op.create_table(
        "images",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("path", sa.Text, nullable=False),
        sa.Column("desc", sa.String(300)),
        sa.Column(
            "message_id",
	        sa.Integer,
	        sa.ForeignKey("messages.id", ondelete="CASCADE"),
            nullable=False
        ),
    )
    op.create_table(
        "conversations_users_associations",
        sa.Column(
            "conversation_id",
	        sa.Integer,
	        sa.ForeignKey("conversations.id", ondelete="CASCADE")
        ),
        sa.Column(
            "user_id",
	        sa.Integer,
	        sa.ForeignKey("users.id", ondelete="CASCADE")
        ),
    )


def downgrade() -> None:
    remove_list = (
        "conversations_users_associations",
        "images",
        "messages",
        "group_messages",
        "conversations",
    )
    for table in remove_list:
        op.drop_table(table)
