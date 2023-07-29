"""Add user_id column to posts table

Revision ID: 5c73cea24927
Revises: 
Create Date: 2023-07-30 00:43:39.687341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c73cea24927'
down_revision = None
branch_labels = None
depends_on = None


# Reference to the 'users' table
users_table = sa.Table('users', sa.MetaData(), sa.Column('id', sa.Integer, primary_key=True))

def upgrade():
    # Add the 'user_id' column to the 'posts' table
    op.add_column('posts', sa.Column('user_id', sa.Integer, sa.ForeignKey(users_table.c.id), nullable=False))

def downgrade():
    # Drop the 'user_id' column from the 'posts' table
    op.drop_column('posts', 'user_id')