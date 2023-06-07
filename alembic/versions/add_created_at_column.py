"""Add created_at column

Revision ID: revision_id
Revises: 
Create Date: create_date

"""

from alembic import op
import sqlalchemy as sa
import urllib.parse
from sqlalchemy import create_engine
from datetime import datetime

revision_id = datetime.now().strftime("%Y%m%d%H%M%S")
create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Set the revision ID and create date
revision = revision_id
down_revision = None
create_date = create_date
# Encode the password with urllib.parse.quote_plus()

password = urllib.parse.quote_plus('p@ssw0rd')
# Create the connection string with the encoded password
connection_string = f'postgresql://postgres:{password}@localhost/postgres'

# Create the engine
engine = create_engine(connection_string)

# The table name and column name need to be adjusted according to your existing table structure
table_name = 'users'
column_name = 'created_at'

# The upgrade() function should contain the logic to add the created_at column to the user table:
def upgrade():
    op.add_column(table_name, sa.Column(column_name, sa.DateTime, nullable=True))

# The downgrade() function should contain the logic to remove the created_at column from the user table:
def downgrade():
    op.drop_column(table_name, column_name)

# Run upgrade() using `alembic upgrade head`
# run downgrade() -> `alembic downgrade base`