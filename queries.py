import sqlite3

def get_db_connection():
    connection = sqlite3.connect('database.db')
    return connection

def get_all_todos():
    connection = get_db_connection()
    todos = connection.execute('SELECT * FROM todos').fetchall()
    connection.close()
    return todos

def add_todo(title):
    connection = get_db_connection()
    connection.execute('INSERT INTO todos (title) VALUES (?)', (title , ))
    connection.commit()
    connection.close()
