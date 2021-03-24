import pyodbc

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = pyodbc.connect(server='cloudthingsdb.database.windows.net', user='cloudthingsadmin', password='MVCM7qs7BQ62Ci4', database='cloudthings', driver= '{ODBC Driver 17 for SQL Server}')
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    print(posts)
    return render_template('index.html', posts=posts)


