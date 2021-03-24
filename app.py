import pyodbc

from flask import Flask, render_template
from azure.appconfiguration import AzureAppConfigurationClient

connection_str = "CloudThingsConnection"
client = AzureAppConfigurationClient.from_connection_string(connection_str)

app = Flask(__name__)

@app.route('/')
def index():

    conn = pyodbc.connect(server='cloudthingsdb.database.windows.net', user='cloudthingsadmin', password='MVCM7qs7BQ62Ci4', database='cloudthings', driver= '{ODBC Driver 17 for SQL Server}')
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


