import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
               )
''')

#cursor.execute('INSERT INTO todos (title) VALUES ("Помыть посуду")')
#cursor.execute('INSERT INTO todos (title) VALUES ("Сделать уроки")')

connection.commit()
connection.close()

print('База данных создана!')