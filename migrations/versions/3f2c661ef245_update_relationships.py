"""Update relationships

Revision ID: 3f2c661ef245
Revises: 5d32a8418814
Create Date: 2024-12-18 22:38:41.001483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection


# revision identifiers, used by Alembic.
revision: str = '3f2c661ef245'
down_revision: Union[str, None] = '5d32a8418814'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = reflection.Inspector.from_engine(conn)

    # Check if 'users' table exists
    if 'users' not in inspector.get_table_names():
        op.create_table(
            'users',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('email', sa.String, unique=True, nullable=False),
        )

    # Check if 'goals' table exists
    if 'goals' not in inspector.get_table_names():
        op.create_table(
            'goals',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
            sa.Column('target_type', sa.String, nullable=False),
            sa.Column('target_value', sa.Float, nullable=False),
            sa.Column('deadline', sa.Date, nullable=False),
        )


def downgrade() -> None:
    op.drop_table('goals')
    op.drop_table('users')
