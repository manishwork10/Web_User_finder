from importlib.resources import path
import os
import sqlite3 as db
def register_user(input_dict):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLPATH = os.path.join(BASE_DIR, 'database.db')

    conn = db.connect(SQLPATH)
    conn.execute('INSERT INTO users (username, phonenumber) VALUES (?, ?)', (input_dict['username'], input_dict['phonenumber']))
    conn.commit()
    conn.close()
    