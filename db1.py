import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "postgres",
    user = "postgres",
    password = "p@ssw0rd"
)
cursor = conn.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        password VARCHAR(100)
    );
"""
cursor.execute(create_table_query)

insert_values = """
    INSERT INTO users(username,email,password) 
    VALUES(%s,%s,%s) 
"""

data = [
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3'),
    ('user4', 'user4@example.com', 'password4')
]

cursor.executemany(insert_values,data)
# Execute SQL queries
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    name = row[1]
    email = row[2]
    password = row[3]
    # Perform any required operations with the retrieved data
    print(f"Username: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print()


# Commit changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()