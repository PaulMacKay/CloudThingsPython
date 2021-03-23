from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "CloudThings Website connected to VS Code test 2"
