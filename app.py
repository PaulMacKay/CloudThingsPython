import pyodbc

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #conn = pyodbc.connect(server='cloudthingsdb.database.windows.net', user='cloudthingsadmin', password='MVCM7qs7BQ62Ci4', database='cloudthings', driver= '{ODBC Driver 17 for SQL Server}')
    #posts = conn.execute('SELECT * FROM posts').fetchall()
    #conn.close()
    #print(posts)
    posts="[(1, datetime.datetime(2021, 3, 24, 1, 20, 6, 610000), 'First Post', 'Content for the first post'), (2, datetime.datetime(2021, 3, 24, 1, 20, 6, 613000), 'Second Post', 'Content for the second post')]]"
    return render_template('index.html', posts=posts)


