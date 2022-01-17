import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO income_type (income_type) VALUES (?)", ("active",))
cursor.execute("INSERT INTO income_type (income_type) VALUES (?)", ("passive",))

connection.commit()
connection.close()    