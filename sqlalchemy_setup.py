import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Encode the password with urllib.parse.quote_plus()
password = urllib.parse.quote_plus('p@ssw0rd')
# Create the connection string with the encoded password
connection_string = f'postgresql://postgres:{password}@localhost/postgres'

# Create the engine
engine = create_engine(connection_string)
# engine = create_engine('postgresql://username:password@localhost/mydatabase')
#Establish a Database Connection
# engine = create_engine('postgresql://postgres:{password}@localhost/postgres')

# Define a Base Model -This base model class will provide common functionality and configuration
Base = declarative_base()

#Define Models - Each class represents a table in the database, and each attribute represents a column
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
# Create Tables- SQLAlchemy provides a feature called "schema generation" that can automatically create the tables based on your model definitions.

Base.metadata.create_all(engine)

# Create a Session- The session object acts as a middleman between your code and the database
Session = sessionmaker(bind=engine)
session = Session()
