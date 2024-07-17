from flask import Flask

app = Flask(__name__)

@app.route("/<str:name>")
def hello_world(name):
    return "<p>vanakkam da maple {name}</p>"