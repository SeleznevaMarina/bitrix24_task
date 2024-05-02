"""migration_1

Revision ID: 98f11604272a
Revises: 
Create Date: 2024-04-29 13:03:57.689677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98f11604272a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'names_woman',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False)
    )

    op.create_table(
        'names_man',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('names_woman')
    op.drop_table('names_man')
