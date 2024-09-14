"""
alter_conversation_table

Revision ID: b0090efbf177
Revises: 54d5cd4ba93f
Create Date: 2024-09-14 20:43:08.984326

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0090efbf177'
down_revision: str | None = '54d5cd4ba93f'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("conversations") as batch_op:
        batch_op.add_column(
            sa.Column(
                "name",
                sa.String(200),
                nullable=False
            )
        )
        batch_op.add_column(
            sa.Column(
                "photo",
                sa.Text
            )
        )


def downgrade() -> None:
    with op.batch_alter_table("conversations") as batch_op:
        batch_op.drop_column("name")
        batch_op.drop_column("photo")
