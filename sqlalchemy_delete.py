from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Post
import urllib

password = urllib.parse.quote_plus("p@ssw0rd")
connection_string = f'postgresql://postgres:{password}@localhost/postgres'
engine = create_engine(connection_string)
Session = sessionmaker(bind = engine)
session = Session()

post_id = 21
post = session.query(Post).get(post_id)
if post is not None:
    val = post.title
    session.delete(post)
    session.commit()
    print(f"'{val} ' deleted Successfully")
else:
    print("Post not found")


# Specify the condition for the deletion
condition = Post.content == "Content of post 5"
num_deleted = session.query(Post).filter(condition).delete()
session.commit()
session.close()

print(f"{num_deleted} rows deleted.")
# posts = session.query(Post).all()
# for post in posts:
#     print(f'title : {post.title}')
#     print(f"content : {post.content}")
#     print("-------")

