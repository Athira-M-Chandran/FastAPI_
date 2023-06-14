
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import ProgrammingError
import urllib

password = urllib.parse.quote_plus("p@ssw0rd")
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Specify the table to drop
table_name = 'users'

# Drop the table using a session
try:
    drop_statement = text(f"DROP TABLE IF EXISTS {table_name}")
    session.execute(drop_statement)
    session.commit()
    print("Table dropped successfully.")
except ProgrammingError as e:
    print(f"Error occurred while dropping table: {e}")

# Close the session
session.close()