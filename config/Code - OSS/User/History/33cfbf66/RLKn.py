from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return "vanakkam da maple {name}"
@app.route("/hello")
def hello():
    return "this is helloworld"