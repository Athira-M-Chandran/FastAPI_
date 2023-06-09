from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Post
import urllib

password = urllib.parse.quote_plus('p@ssw0rd')
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
session = Session()

post1 = Post(title='First Post', content='This is the content of the first post.')
post2 = Post(title='Second Post', content='This is the content of the second post.')

session.add(post1)
session.add(post2)

session.commit()
session.close()