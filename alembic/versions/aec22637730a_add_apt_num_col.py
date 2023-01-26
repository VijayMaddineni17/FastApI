"""Add apt num col

Revision ID: aec22637730a
Revises: 69ba357a865c
Create Date: 2023-01-25 16:23:09.827074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aec22637730a'
down_revision = '69ba357a865c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address',sa.Column('apt_num',sa.Integer(),nullable=True))


def downgrade() -> None:
    op.drop_column('address','apt_num')
