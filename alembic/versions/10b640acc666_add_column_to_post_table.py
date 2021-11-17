"""Add column to post table

Revision ID: 10b640acc666
Revises: 59ee2beceecb
Create Date: 2021-11-16 16:03:51.848963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b640acc666'
down_revision = '59ee2beceecb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
