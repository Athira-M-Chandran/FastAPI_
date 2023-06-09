from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Post
import urllib

password = urllib.parse.quote_plus("p@ssw0rd")
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
session = Session()

post_id = 10
post = session.query(Post).get(post_id)

if post is not None:
    print(f'title : {post.title}')
    print(f'post : {post.content}')
else:
    print("Post not found.")

# with where condition
post_content = "Content of post 4"
filter_post = session.query(Post).filter_by(content=post_content).all()  # .first() will retrieve first value

for post in  filter_post:
    print(f"id: {post.id}")
    print(f'title : {post.title}')
    print(f'post : {post.content}')
    print("---")


session.close()