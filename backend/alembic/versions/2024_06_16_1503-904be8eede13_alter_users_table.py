"""
Alter users table, add photo column

Revision ID: 904be8eede13
Revises: 050124699917
Create Date: 2024-06-16 15:03:00.475853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '904be8eede13'
down_revision: Union[str, None] = '050124699917'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(sa.Column("photo", sa.String(500)))

def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column("photo")
