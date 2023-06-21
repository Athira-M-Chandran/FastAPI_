import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

password = urllib.parse.quote_plus('p@ssw0rd')
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
# session = Session()
