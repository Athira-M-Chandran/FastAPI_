from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str

posts = [
    Post(id=1, title="First Post", content="This is the content of the first post"),
    Post(id=2, title="Second Post", content="This is the content of the second post"),
    # Add more posts here
]

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    return {"message": "Post not found"}