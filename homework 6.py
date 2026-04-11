import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

def create_user(name, email, age):
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def update_user(user_id, name, email, age):
    cursor.execute("UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?", (name, email, age, user_id))
    conn.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def create_post(title, content, user_id):
    cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, user_id))
    conn.commit()

def get_posts_by_user(user_id):
    cursor.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

create_user("Alex", "alex@gmail.com", 20)
create_user("Bob", "bob@gmail.com", 25)

print(get_users())

update_user(1, "Alex Updated", "alex2@gmail.com", 21)

print(get_user(1))

delete_user(2)

print(get_users())

create_post("Post 1", "Content 1", 1)
create_post("Post 2", "Content 2", 1)

print(get_posts_by_user(1))

conn.close()
