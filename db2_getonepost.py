import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "postgres",
    user = "postgres",
    password = "p@ssw0rd"
)

cursor = conn.cursor()

create_query = """
CREATE TABLE IF NOT EXISTS posts(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    content TEXT

);
"""
cursor.execute(create_query)
conn.commit()

insert_query ="""
INSERT INTO posts(title,content)
VALUES(%s,%s)
"""

# Define the data for the rows to be inserted
data = [
    ("Post 1", "Content of post 1"),
    ("Post 2", "Content of post 2"),
    ("Post 3", "Content of post 3"),
    ("Post 4", "Content of post 4"),
    ("Post 5", "Content of post 5")
]

cursor.executemany(insert_query,data)

conn.commit()

select_full_query = """SELECT * FROM posts"""
cursor.execute(select_full_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

select_query = """
SELECT *
FROM posts
WHERE id = %s
"""
value = 12
cursor.execute(select_query,(value,))
row = cursor.fetchone()
if row:
    print(f"post id : {row[0]}")
    print(f"title : {row[1]}")
    print(f"content : {row[2]}")
else:
    print("Post not found")

cursor.close()
conn.close()