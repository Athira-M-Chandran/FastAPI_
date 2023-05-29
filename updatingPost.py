from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

class Post(BaseModel):
    id: int
    title : str
    content: str

posts =[
    {"id" : 1, "title": "Post1", "content": "Content1" },
    {"id": 2, "title" : "Post2", "content" : "Content2"},
    {"id": 3, "title" : "Post3", "content" : "Content3"}
]

@app.put("/posts/{post_id}")
def updated_post(post_id: int , updated_post: Post):
    for i, post in enumerate(posts):
        if post["id"]    == post_id:
            posts[i] = updated_post
            return {"message": "Post updated successfully", "Updated post": updated_post, "All posts": posts}
    raise HTTPException(status_code=404, detail = "Post not found")

