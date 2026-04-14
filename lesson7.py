# import sqlite3

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )
# ''')

# conn.commit()




# cursor.execute("INSERT INTO users(name, age) VALUES (?, ?)", ('ERNIAZ', 14))

# conn.commit()


# cursor.execute('SELECT * FROM users')

# users = cursor.fetchall()

# for user in users:
#     print(users)



# cursor.execute('''UPDATE users SET age = ? WHERE name = ?''', (17,'erniaz'))



# cursor.execute('SELECT * FROM users')

# users = cursor.fetchall()

# for user in users:
#     print(users)


#     cursor.execute('''DELETE FROM users WHERE name = ?''', ('erniaz',))


# cursor.execute('SELECT * FROM users')

# users = cursor.fetchall()

# for user in users:
#     print(users)

# conn.close()




import sqlite3

db = sqlite3.connect('collection.db')
cursor = db.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    name TEXT
)''')



cursor.execute("INSERT INTO items (title, description, name) VALUES (?, ?, ?)", ('gg', 'описание 1', 'имя 1'))
cursor.execute("INSERT INTO items (title, description, name) VALUES (?, ?, ?)", ('kk', 'описание 2', 'имя 2'))
db.commit()



cursor.execute("SELECT * FROM items")
for item in cursor.fetchall():
    print(item)




cursor.execute("UPDATE items SET title = ? WHERE id = ?", ('обновлено', 1))
db.commit()




cursor.execute("DELETE FROM items WHERE id = ?", (2,))
db.commit()



db.close()


