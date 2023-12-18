"""Renaming email to email_address

Revision ID: 3fa9cd8de35a
Revises: 791279dd0760
Create Date: 2023-12-19 00:17:07.840195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa9cd8de35a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='email_address')


def downgrade() -> None:
    op.alter_column('students', 'email_address', new_column_name='email')
