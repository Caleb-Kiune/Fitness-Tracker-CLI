"""Add user table

Revision ID: 8ccdac48db38
Revises: deedaee1b280
Create Date: 2024-12-18 21:17:17.719046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ccdac48db38'
down_revision: Union[str, None] = 'deedaee1b280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass  # This migration doesn't need to do anything as the users table is already created


def downgrade() -> None:
    pass  # No need to drop the users table here
