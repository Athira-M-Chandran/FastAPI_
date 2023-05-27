from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PostCreate(BaseModel):
    title: str
    content : str

class Post(BaseModel):
    id: int
    title: str
    content: str

posts = []

@app.post("/posts/")
def create_post(post_data : PostCreate):
    post_id = len(posts) +1
    post = Post(id= post_id, title = post_data.title, content=post_data.content)
    posts.append(post)
    return {"message" : "Post created sucessfully", "post" : post}

@app.get("/posts/")
def get_posts():
    return {"posts": posts}
