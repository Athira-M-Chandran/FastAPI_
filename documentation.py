from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from pydantic import BaseModel


app = FastAPI()
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



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " - Swagger UI"
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title=app.title + " - ReDoc"
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )
