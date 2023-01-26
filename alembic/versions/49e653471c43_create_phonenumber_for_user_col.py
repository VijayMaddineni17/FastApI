"""create phonenumber for user col

Revision ID: 49e653471c43
Revises: 
Create Date: 2023-01-25 12:37:36.580965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49e653471c43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
