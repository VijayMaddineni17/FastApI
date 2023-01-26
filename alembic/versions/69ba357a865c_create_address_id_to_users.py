"""Create address_id to users

Revision ID: 69ba357a865c
Revises: 25422ecdde5e
Create Date: 2023-01-25 13:18:37.030018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ba357a865c'
down_revision = '25422ecdde5e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column('address_id',sa.Integer(),nullable=True))
    op.create_foreign_key('address_users_fk',source_table='users',referent_table='address',local_cols=['address_id']
                          ,remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk',table_name="users")
    op.drop_column('users','address_id')
