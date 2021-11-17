"""auto-votes

Revision ID: db7ba1a323f9
Revises: 1cfc806bbd09
Create Date: 2021-11-17 11:39:16.374685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db7ba1a323f9'
down_revision = '1cfc806bbd09'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id'),
                    )


def downgrade():
    op.drop_table('votes')
