"""
alter_tel_type_in_users_table

Revision ID: 6317a41559b7
Revises: 944f9a1ad75c
Create Date: 2024-07-19 13:33:47.909377

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6317a41559b7'
down_revision: str | None = '944f9a1ad75c'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column("tel", type_=sa.String(30))


def downgrade() -> None:
    pass
