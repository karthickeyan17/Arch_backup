from flask import Flask

app = Flask(__name__)

@app.route("/g/<str:name>")
def hello_world(name):
    return f"vanakkam da maple {name}"
@app.route("/hello")
def hello():
    return "this is helloworld"