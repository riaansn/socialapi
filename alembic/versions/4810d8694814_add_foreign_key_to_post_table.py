"""add foreign-key to post table

Revision ID: 4810d8694814
Revises: e6b9b1b23df9
Create Date: 2021-11-17 10:49:59.518603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4810d8694814'
down_revision = 'e6b9b1b23df9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
