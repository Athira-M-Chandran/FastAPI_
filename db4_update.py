import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "postgres",
    user = "postgres",
    password = "p@ssw0rd"
)

cursor = conn.cursor()

select_query = """
Select *
from posts
where id = %s"""
id = 3
cursor.execute(select_query,(id,))
row = cursor.fetchone()
update_query = """
update posts
set title = %s, content = %s
where id= %s
returning *
"""

title = "updated title"
content = "updated content"
id = 3

cursor.execute(update_query,(title,content,id))
cursor.execute(select_query,(id,))
row1 = cursor.fetchone()

if(row):
    print(f"going to update : {row}")
if(row1):
    print(f"updated row : {row1}")

conn.commit()
cursor.close()
conn.close()
