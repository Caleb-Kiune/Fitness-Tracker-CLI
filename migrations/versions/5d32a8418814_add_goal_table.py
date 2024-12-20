"""Add goal table

Revision ID: 5d32a8418814
Revises: 8ccdac48db38
Create Date: 2024-12-18 21:38:41.001483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d32a8418814'
down_revision: Union[str, None] = '8ccdac48db38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'goals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('target_type', sa.String),
        sa.Column('target_value', sa.Integer),
        sa.Column('deadline', sa.Date),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goals')
    # ### end Alembic commands ###
