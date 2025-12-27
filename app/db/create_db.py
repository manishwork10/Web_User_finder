import sqlite3 as db
 
conn = db.connect('database.db')
 
create_user_table = '''CREATE TABLE IF NOT EXISTS users 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    phonenumber TEXT NOT NULL
)'''

cursor = conn.cursor()
cursor.execute(create_user_table)
conn.commit()
cursor.close()
conn.close()