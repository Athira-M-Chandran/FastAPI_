from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Post
import urllib

password = urllib.parse.quote_plus("p@ssw0rd")
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
session = Session()
posts = session.query(Post).all()

for post in posts:
    print(f'title : {post.title}')
    print(f"content : {post.content}")
    print("-------")
session.close()
