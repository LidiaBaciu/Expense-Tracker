import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO user (username, password, email, birthday) VALUES (?, ?, ?, ?)", ("lidia901", "password", "lidia.baciu97@gmail.com", "19.10.1997"))

connection.commit()
connection.close()    