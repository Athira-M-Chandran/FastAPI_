import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "postgres",
    user = "postgres",
    password = "p@ssw0rd"
)

cursor = conn.cursor()

delete_query = """
DELETE 
FROM posts 
WHERE id = %s
RETURNING *
"""
post_id = 13

cursor.execute(delete_query,(post_id,))

select_query = """
select * from posts"""
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
cursor.close()
conn.close()