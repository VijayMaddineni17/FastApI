"""Create Address Table

Revision ID: 25422ecdde5e
Revises: 49e653471c43
Create Date: 2023-01-25 13:07:18.704282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25422ecdde5e'
down_revision = '49e653471c43'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',sa.Column('id',sa.Integer(), nullable=False, primary_key=True),
sa.Column('address1',sa.String(),nullable=False),
sa.Column('address2',sa.String,nullable=False),
sa.Column('city',sa.String,nullable=False),
sa.Column('state',sa.String,nullable=False),
sa.Column('country',sa.String,nullable=False),
sa.Column('postalcode',sa.String,nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
