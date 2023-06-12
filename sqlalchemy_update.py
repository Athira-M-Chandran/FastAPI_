from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Post
import urllib

password = urllib.parse.quote_plus('p@ssw0rd')
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)

Session = sessionmaker(bind = engine)
session = Session()

post_id =1
post = session.query(Post).get(post_id)

if post is not None:
    post.title = "Updated Title"
    session.commit()
    print(f"post id : {post.id} with content : {post.content} is updated successfully")
else:
    print("Post not found")

session.close()
