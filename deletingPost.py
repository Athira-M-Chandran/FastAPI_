from fastapi import FastAPI, HTTPException


app = FastAPI()

posts =[
    {"id" : 1, "title": "Post1", "content": "Content1" },
    {"id": 2, "title" : "Post2", "content" : "Content2"},
    {"id": 3, "title" : "Post3", "content" : "Content3"}
]

@app.delete("/posts/{post_id}")
def delete_post(post_id : int):
    for i,post in enumerate(posts):
        if(post['id'] == post_id):
            deleted_post = posts.pop(i)
            return {"message": "Post deleted successfully", "deleted post": deleted_post, "posts":posts}
    raise HTTPException(status_code=404, detail = "Post not found" )