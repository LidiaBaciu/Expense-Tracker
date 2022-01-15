import sqlite3
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('database.db')
    # Allow name-based access to columns
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM user').fetchall()
    conn.close()
    print('added some changes here to check git changing username')
    return render_template('index.html', users=users)

@app.route("/user/income/<name>")
def get_income_type(name):
    return "name: {}".format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')