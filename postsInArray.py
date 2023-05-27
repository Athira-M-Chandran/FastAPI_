from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Post(BaseModel):
    id : int
    title: str
    content : str

posts = []

@app.post("/posts/")
def post_content(post : Post):
    posts.append(post)
    return{"message":"post created succesfully", "posts": posts}

@app.get("/get_post/")
def get_post():
    return {"posts" : posts}
    
@app.get("/get_posts/{post_id}")
def get_posts(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    return {"Message": "Post not found"}