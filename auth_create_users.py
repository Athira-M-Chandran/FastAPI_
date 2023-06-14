from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auth_model_users import Base, User
import urllib

password = urllib.parse.quote_plus('p@ssw0rd')
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
session = Session()
Base.metadata.create_all(engine)

session.close()