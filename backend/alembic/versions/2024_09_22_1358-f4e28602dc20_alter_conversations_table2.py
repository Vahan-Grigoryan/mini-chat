"""
alter_conversations_table2

Revision ID: f4e28602dc20
Revises: b0090efbf177
Create Date: 2024-09-22 13:58:46.500502

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import true


# revision identifiers, used by Alembic.
revision: str = 'f4e28602dc20'
down_revision: str | None = 'b0090efbf177'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("conversations") as batch_op:
        batch_op.add_column(
            sa.Column(
                "private",
                sa.Boolean,
                server_default=true(),
                nullable=False
            )
        )
        batch_op.add_column(
            sa.Column(
                "admin_id",
                sa.Integer,
                sa.ForeignKey("users.id", ondelete="CASCADE"),
                nullable=False
            )
        )
    op.create_index(
        "public_convs_are_unique",
        "conversations",
        ["name"],
        unique=True,
        postgresql_where=("not private")
    )


def downgrade() -> None:
    with op.batch_alter_table("conversations") as batch_op:
        batch_op.drop_column("private")
        batch_op.drop_column("admin_id")
