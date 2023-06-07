from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

def  get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database ="postgres",
        user = "postgres",
        password = "p@ssw0rd"
    )
    return conn

class PostCreate(BaseModel):
    title : str
    content : str

app = FastAPI()

@app.post("/createPosts/")
def create_posts(post : PostCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO posts(title,content)
    VALUES(%s,%s)
    """
    title = post.title
    content = post.content

    cursor.execute(query,(title,content))
    connection.commit()
    cursor.close()
    connection.close()
    return{"message" : "posted successfully"}

@app.get("/posts/")
def get_post():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    posts = [PostCreate(id = row[0], title=row[1],content= row[2]) for row in rows]
    
    cursor.close()
    connection.close()
    return {"posts" : posts}