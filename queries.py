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

def delete_todo(task_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM todos WHERE id = ?', (task_id , ))
    connection.commit()
    connection.close()

def toggle_todo(task_id):
    connection = get_db_connection()
    todo = connection.execute('SELECT completed FROM todos WHERE id = ?', (task_id, )).fetchone()
    if todo:
        new_status = 0 if todo[0] else 1
        connection.execute('UPDATE todos SET completed = ? WHERE id = ? ', (new_status, task_id ))
        connection.commit()

    connection.close()
