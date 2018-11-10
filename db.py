import sqlite3
import random

from auth import generate_token, unhash_password, hash_password

DATABASE = 'users.db'

def get_db():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(e)

    return None

def insert_user(username, password, key):
    conn = get_db()
    hashed_password = hash_password(password)
    with conn:
        cur = conn.cursor()
        args = (random.randint(1, 999), username, hashed_password,)
        sql = '''INSERT INTO USERS(ID, USERNAME, PASSWORD) VALUES (?,?,?)'''
        cur.execute(sql, args)
        return login(conn, username, password, key)
    conn.close()

def login(conn, username, password, key):
    if conn == None:
        conn = get_db()
    with conn:
        args = (username,)
        sql = '''SELECT username, password FROM USERS WHERE USERNAME=?'''
        cursor = conn.execute(sql, args)
        user = cursor.fetchone()
        if user == None:
            return "User not found"
        if unhash_password(password, user[1]):
            return generate_token(username, key)
        else:
            return "Some credentials are incorrect. Please try again."
    conn.close()
