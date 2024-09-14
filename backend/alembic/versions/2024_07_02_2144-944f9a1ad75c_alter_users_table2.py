"""
alter_users_table2

Revision ID: 944f9a1ad75c
Revises: 904be8eede13
Create Date: 2024-07-02 21:44:58.449935

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '944f9a1ad75c'
down_revision: str | None = '904be8eede13'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(
            sa.Column(
                "email",
                sa.String(500),
                unique=True,
                nullable=False
            )
        )
        batch_op.add_column(sa.Column("tel", sa.Integer))

def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column("email")
        batch_op.drop_column("tel")
