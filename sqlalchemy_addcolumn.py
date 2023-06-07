from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import urllib.parse
# Encode the password with urllib.parse.quote_plus()
password = urllib.parse.quote_plus('p@ssw0rd')
# Create the connection string with the encoded password
connection_string = f'postgresql://postgres:{password}@localhost/postgres'

# Create the engine
engine = create_engine(connection_string)

# Create the base declarative class
Base = declarative_base()

# Define your model class
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=func.now())

# Create the table in the database
Base.metadata.create_all(engine)
