import pymssql  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = pymssql.connect(server='cloudthingsdb.database.windows.net', user='cloudthingsadmin', password='MVCM7qs7BQ62Ci4', database='cloudthings')
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
