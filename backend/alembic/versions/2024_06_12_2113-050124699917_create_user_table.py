"""
Create users table

Revision ID: 050124699917
Revises: 
Create Date: 2024-06-12 21:13:21.931375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '050124699917'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("age", sa.Integer),
        sa.Column("password", sa.String(200), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
